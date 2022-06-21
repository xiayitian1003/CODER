//package com.smartcallerpro.OSV8.calldetail;
//
//import static com.smartcallerpro.OSV8.calldetail.CallDetailsUtil.getColorWithAlpha;
//
//import android.app.Activity;
//import android.graphics.Paint;
//import android.net.Uri;
//import android.text.Layout;
//import android.text.SpannableString;
//import android.text.Spanned;
//import android.text.TextUtils;
//import android.text.style.ForegroundColorSpan;
//import android.util.Pair;
//import android.view.View;
//import android.widget.Button;
//import android.widget.FrameLayout;
//import android.widget.ImageView;
//import android.widget.TextView;
//
//import androidx.annotation.NonNull;
//import androidx.constraintlayout.widget.ConstraintLayout;
//
//import com.android.dialer.R;
//import com.android.dialer.app.calllog.DialerQuickContactBadge;
//import com.android.dialer.calldetails.OldCallDetailsActivity;
//import com.android.dialer.common.LogUtil;
//import com.android.dialer.contactphoto.ContactPhotoManager;
//import com.android.dialer.dialercontact.DialerContact;
//import com.android.dialer.util.UriUtils;
//import com.android.dialer.util.ViewUtil;
//import com.google.android.material.appbar.AppBarLayout;
//import com.smartcallerpro.OSV8.Athana.AthenaLogUtil;
//import com.smartcallerpro.OSV8.CallFilter.harass.blocknumber.sdk.OSV8SpamNumberUtil;
//import com.smartcallerpro.OSV8.CallFilter.harass.blocknumber.sdk.spamlabel.Dialog.OS8SpamLabelDialog;
//import com.smartcallerpro.OSV8.PlatformCompact.OSAndPlatformOption;
//import com.smartcallerpro.theme.ThemeMgr;
//import com.smartcallerpro.utils.OSCallFilterCompat;
//import com.trans.phone.extuitls.util.ScreenUtils;
//import com.trans.phone.extuitls.util.SizeUtils;
//
///**
// * @ClassName: CallDetailHeaderManager
// * @Description:
// * @Author: jinxin.zhou
// * @CreateDate: 2020/12/21 19:17
// */
//
//public class CallDetailHeaderManager {
//    private Activity mActivity;
//    private ImageView mBlockIcon;
//    private DialerQuickContactBadge mPhoto;
//    private Button mSpamLabelBtn;
//    private TextView mNameOrNumber;
//    private String mContactUri;
//    private long mPhotoId;
//    private String mPhotoUri;
//    private int mContactType;
//    private String mLocalContactsName;
//    private String mContactName;
//    private String mContactAltName;
//    public final static String TAG = "CallDetailHeaderManager";
//    private AppBarLayout mAppBarLayout;
//    private TextView mTitleName;
//    private final static int FIRST_NAME = 0;
//    private final static int LAST_NAME = 1;
//    private OS8CallDetailBkgView mRootView;
//    private boolean mContactHasAvatar;
//    private boolean mIsXOS;
//    private boolean mHasName;
//    private boolean mIsBlock;
//    private String mNumber;
//    private String lookupKey;
//    private boolean isSaveContact;
//
//    private float mTitleTransY;
//    private TextView mMockName;
//    private String extraMockStr = "";
//    private int nameAndMockTansX;//名字动画过程中，X轴的变化距离，暂时只对 有头像的 情况做X轴动画。
//    // 无头像界面由于缩小加位移后 位置也差不多了，如果需要微调后面再说
//
//    public CallDetailHeaderManager(Activity activity) {
//        mActivity = activity;
//    }
//
//    public void updateHeadView(DialerContact contact) {
//        //变量初始化
//        mContactUri = contact.getContactUri();
//        mPhotoId = contact.getPhotoId();
//        mPhotoUri = contact.getPhotoUri();
//        mContactType = contact.getContactType();
//        mLocalContactsName = contact.getNameOrNumber();
//        mContactName = contact.getContactName();
//        mContactAltName = contact.getContactNameAlternative();
//        mContactHasAvatar = contact.getPhotoId() != 0 || !TextUtils.isEmpty(contact.getPhotoUri());
//        mIsXOS = ThemeMgr.AppThemeType.equals(OSAndPlatformOption.OsType.XOS);
//        mHasName = !TextUtils.isEmpty(mContactName);
//        mIsBlock = ((OldCallDetailsActivity) mActivity).isBlocked;
//        mNumber = contact.getNumber();
//
//        //zjx: for colorful head bkg
//        if (TextUtils.isEmpty(mContactUri)) {
//            isSaveContact = false;
//        } else {
//            isSaveContact = !UriUtils.isEncodedContactUri(Uri.parse(mContactUri));
//        }
//
//
//        lookupKey = TextUtils.isEmpty(mContactUri) ? mLocalContactsName : UriUtils.getLookupKeyFromUri(Uri.parse(mContactUri));
//
//        updateHeadView();
//    }
//
//    private void updateHeadView() {
//        /*-----------------------------View 初始化---------------------------------------------*/
//        FrameLayout mContainer = mActivity.findViewById(R.id.call_detail_head_container);
//        //resize 重新设置不同os 的head高度。动态inflate  xml定义高度无效
//        CallDetailsUtil.reSizeHeadSize(mContainer, ThemeMgr.AppThemeType, mContactHasAvatar);
//
//        //定义不同os 动态加载的view
//        int HeadLayoutId = CallDetailsUtil.getOSHeadLayoutID(ThemeMgr.AppThemeType, mContactHasAvatar);
//        if (HeadLayoutId == 0) {
//            LogUtil.i(TAG, "resolver os layout error");
//            return;
//        }
//        View headView = View.inflate(mActivity, HeadLayoutId, null);
//
//        //other view 初始化其他view
//        mAppBarLayout = mActivity.findViewById(R.id.call_detail_appbar);
//        mTitleName = mActivity.findViewById(R.id.call_detail_contact_title_name);
//        mRootView = ((OldCallDetailsActivity) mActivity).mRootView;
//
//        //head view 初始化 head里面的view
//        mMockName = mActivity.findViewById(R.id.mock_name_or_num);
//        mMockName.setTextDirection(View.TEXT_DIRECTION_LTR);
//
//        mNameOrNumber = headView.findViewById(R.id.call_detail_name_or_num);
//        mNameOrNumber.setTextDirection(View.TEXT_DIRECTION_LTR);
//        if (mContactHasAvatar) {
//            mPhoto = headView.findViewById(R.id.call_detail_photo);
//        }
//
//        mSpamLabelBtn = headView.findViewById(R.id.call_details_spam_type);
//
//        if (OSCallFilterCompat.isUseOSOptionCallFilter()) {
//            mSpamLabelBtn.setVisibility(mIsBlock ? View.VISIBLE : View.GONE);
//        } else {
//            mSpamLabelBtn.setVisibility(View.GONE);
//        }
//
//        mSpamLabelBtn.setText(OSV8SpamNumberUtil.resolverSpamType(OSV8SpamNumberUtil.getSpamType(mNumber), mActivity));
//        mSpamLabelBtn.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View v) {
//                new OS8SpamLabelDialog(mActivity, null)
//                        .setSpamNumber(mNumber)
//                        .setOnBlockCompleteListener(() -> ((OldCallDetailsActivity) mActivity).updateView())
//                        .show();
//
//                AthenaLogUtil.logEvent(101460000226L, "bla_list_sign_show", Pair.create("source", "modify"));
//            }
//        });
//        /*-----------------------------View 初始化完毕---------------------------------------------*/
//
//        //更新head 数据
//        updateHeadData();
//
//        //将动态创建完毕的head 添加进详情页
//        mContainer.removeAllViews();
//        mContainer.addView(headView);
//    }
//
//    private void updateHeadData() {
//        //如果有头像就设置头像
//        if (mPhoto != null) {
//            mPhoto.setClickable(false);
//        }
//
//        if (mPhoto != null) {
//            ContactPhotoManager.getInstance(mActivity)
//                    .loadDialerThumbnailOrPhoto(
//                            mPhoto,
//                            mContactUri.isEmpty() ? null : Uri.parse(mContactUri),
//                            mPhotoId,
//                            mPhotoUri.isEmpty() ? null : Uri.parse(mPhotoUri),
//                            mLocalContactsName,
//                            mContactType);
//        }
//
//        if (!mContactHasAvatar) {
//            mRootView.drawOSBkg(lookupKey, isSaveContact);
//        } else {
//            mRootView.removeBkg();
//        }
//
//        mNameOrNumber.setText(CallDetailsUtil.formatCallDetailsNameV2(mContactName,
//                mContactAltName,
//                mLocalContactsName));
//
////        mMockName.setText(mNameOrNumber.getText());
//        mTitleName.setText(mNameOrNumber.getText());
//
//        ViewUtil.doOnGlobalLayout(mTitleName, new ViewUtil.ViewRunnable() {
//            @Override
//            public void run(@NonNull View view) {
//                //mMockName 是一个虚假的占位，用来覆盖在 name 上面，做全程的动画
//                //首先设置大小以及位置 和 mNameOrNumber 一模一样
//                FrameLayout.LayoutParams mockNameLp = (FrameLayout.LayoutParams) mMockName.getLayoutParams();
//                mockNameLp.height = mNameOrNumber.getMeasuredHeight();
//                mockNameLp.topMargin = ((ConstraintLayout.LayoutParams) mNameOrNumber.getLayoutParams()).topMargin;
//                mMockName.setLayoutParams(mockNameLp);
//                // mMockName.setTextSize(TypedValue.COMPLEX_UNIT_DIP, SizeUtils.px2dp(mNameOrNumber.getPaint().getTextSize()));
//
//                //
//                Layout layout = mNameOrNumber.getLayout();
//                int start = layout.getLineStart(0);
//                int end = layout.getLineEnd(0);
//                String nameFirstLineText = layout.getText().toString().substring(start, end);
//                //以18dp的大小来获取当前第一行文字的长度
//                Paint paint = new Paint();
//                paint.setTextSize(SizeUtils.dp2px(18));
//                float titleStrWidth = paint.measureText(nameFirstLineText);
//                float titleRemainSpace = mTitleName.getMeasuredWidth() - SizeUtils.dp2px(16) - titleStrWidth;
//                boolean hasExtraStr = mNameOrNumber.getText().length() > nameFirstLineText.length();
//
//
//                //有头像的情况下 名字居中对齐。因此需要计算出  mNameOrNumber 第一行到屏幕边界的距离，然后将 mMockName 加上一个padding
//                if (mContactHasAvatar) {
//                    Paint paint1 = mNameOrNumber.getPaint();
//                    float nameFirstLineWidth = paint1.measureText(nameFirstLineText.trim());
//                    int nameFirstLineMarginScreen = (int) ((ScreenUtils.getScreenWidth() - nameFirstLineWidth) / 2);
//                    mMockName.setPaddingRelative(nameFirstLineMarginScreen,
//                            mMockName.getPaddingTop(),
//                            mMockName.getPaddingRight(),
//                            mMockName.getPaddingBottom());
//                    nameAndMockTansX = nameFirstLineMarginScreen - SizeUtils.dp2px(54);
//                }
//
//                //1.放得下，继续尝试拼接第二行的字符，在上推动画的第二阶段进行 0-1 的alpha动画
//                if (titleRemainSpace > 0) {
//                    // 1.1 放得下第二行有多余的字符
//                    if (hasExtraStr) {
//                        //1.1.1 剩余空间大于18dp, 说明可以继续放字符，继续计算放几个，并且进行拼接
//                        if (titleRemainSpace > SizeUtils.dp2px(18)) {
//                            //标题减掉第一行长度以后，剩余空间可以装下几个字符
//                            int titleCanPlaceStrCount = (int) (titleRemainSpace / SizeUtils.dp2px(18));
//                            //第二行的剩余字符数量 = 总长度减去第一行长度
//                            int extraStrCount = mNameOrNumber.getText().length() - nameFirstLineText.length();
//
//                            //1.1.1.1  第二行的字符数量，大于剩余空间，那就截取 第一行加剩余空间的长度，并拼接三个点
//                            if (extraStrCount > titleCanPlaceStrCount) {
//                                extraMockStr = mNameOrNumber.getText().toString().substring(nameFirstLineText.length(), nameFirstLineText.length() + titleCanPlaceStrCount) + "...";
//                            }
//                            //1.1.1.2  第二行的字符数量 小于剩余空间， 说明完全可以显示下
//                            else {
//                                extraMockStr = mNameOrNumber.getText().toString().substring(nameFirstLineText.length(), nameFirstLineText.length() + extraStrCount);
//                            }
//                        }
//
//                        //1.1.2 如果第二行有剩余的字符 并且剩余空间小于18dp ，那直接拼接 ...
//                        else {
//                            extraMockStr = "...";
//                        }
//                    } else {
//                        // 1.2放得下， 第二行 没有多余的字符，不进行任何处理
//                    }
//
//                    if (!TextUtils.isEmpty(extraMockStr)) {
//                        SpannableString ss = new SpannableString(String.format("%s%s", nameFirstLineText, extraMockStr));
//                        int alphaStart = nameFirstLineText.length();
//                        int alphaEnd = nameFirstLineText.length() + extraMockStr.length();
//                        ss.setSpan(new ForegroundColorSpan(getColorWithAlpha(0, mMockName.getContext().getColor(R.color.os_text_primary_color))),
//                                alphaStart, alphaEnd, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
//                        //，mMockName 直接拼接后的字符
//                        mMockName.setText(ss);
//                    } else {
//                        //，mMockName 直接显示
//                        mMockName.setText(nameFirstLineText);
//                    }
//                }
//
//                //2.放不下  titleSpace < 0 , 就不考虑第二行是不是有字符了，只要判断第一行比推动上去的标题长多少，多了几个字符？
//                else {
//                    extraMockStr = "...";
//                    //2.1 如果第一行比上面长的部分不足18dp，截掉最后一个 换上...
//                    if (Math.abs(titleRemainSpace) < SizeUtils.dp2px(18)) {
//                        //这里暂时多减2位 待后续微调
//                        nameFirstLineText = nameFirstLineText.substring(0, nameFirstLineText.length() - 2 - 1).trim() + extraMockStr;
//                    }
//
//                    //2.2  如果第一行比上面多出来的长度 超过18dp。 计算多了多少个18， 截掉相应的个数 ，再多截一个 （+1 ）换上 '...'
//                    else {
//                        int needSplitStrCount = (int) (Math.abs(titleRemainSpace) / SizeUtils.dp2px(18));
//                        //这里暂时多减2位 待后续微调
//                        nameFirstLineText = nameFirstLineText.substring(0, nameFirstLineText.length() - needSplitStrCount - 2 - 1).trim() + extraMockStr;
//                    }
//                    SpannableString ss = new SpannableString(nameFirstLineText);
//                    int alphaStart = nameFirstLineText.length() - extraMockStr.length();
//                    int alphaEnd = nameFirstLineText.length();
//                    ss.setSpan(new ForegroundColorSpan(getColorWithAlpha(0, mMockName.getContext().getColor(R.color.os_text_primary_color))),
//                            alphaStart, alphaEnd, Spanned.SPAN_EXCLUSIVE_EXCLUSIVE);
//                    //，mMockName 直接拼接后的字符
//                    mMockName.setText(ss);
//                }
//                //设置各个组件的滑动效果
//                setAllComponentsSlideState();
//            }
//        });
//    }
//
//    private void setAllComponentsSlideState() {
//
//        mAppBarLayout.addOnOffsetChangedListener(new AppBarStateChangeListener() {
//            @Override
//            public void onStateChanged(AppBarLayout appBarLayout, State state, int verticalOffset) {
////                float nameSlideRange = CallDetailsUtil.getNameViewSlideRate(ThemeMgr.AppThemeType,
////                        mContactHasAvatar,
////                        mAppBarLayout.getTotalScrollRange());
////                CallDetailsUtil.changeAllComponentsSlideState(state,
////                        verticalOffset,
////                        mContactHasAvatar,
////                        appBarLayout.getTotalScrollRange(),
////                        mNameOrNumber,
////                        mTitleName,
////                        mPhoto,
////                        mRootView,
////                        mLocalContactsName,
////                        nameSlideRange,
////                        mSpamLabelBtn);
//
//                //阻尼系数，名字的缩小不需要和手推的一样快
//                float nameScaleDamp = CallDetailsUtil.OS8_6GetNameViewScaleRate(ThemeMgr.AppThemeType,
//                        mContactHasAvatar,
//                        mAppBarLayout.getTotalScrollRange());
//
//                float nameSlideDamp = CallDetailsUtil.OS8_6GetNameViewSlideRate(ThemeMgr.AppThemeType,
//                        mContactHasAvatar,
//                        mAppBarLayout.getTotalScrollRange());
//
//                float nameTransDamp = CallDetailsUtil.OS8_6GetNameViewTransXRate(ThemeMgr.AppThemeType,
//                        mContactHasAvatar,
//                        mAppBarLayout.getTotalScrollRange(), nameAndMockTansX);
//
//                CallDetailsUtil.OS8_6ChangeAllComponentsSlideState(state,
//                        verticalOffset,
//                        mContactHasAvatar,
//                        appBarLayout.getTotalScrollRange(),
//                        mNameOrNumber,
//                        mMockName,
//                        mPhoto,
//                        mRootView,
//                        extraMockStr,
//                        nameScaleDamp,
//                        nameSlideDamp,
//                        nameAndMockTansX,
//                        nameTransDamp);
//            }
//        });
//    }
//
//    public abstract static class AppBarStateChangeListener implements AppBarLayout.OnOffsetChangedListener {
//        public enum State {
//            EXPANDED,
//            COLLAPSED,
//            IDLE
//        }
//
//        private State mCurrentState = State.IDLE;
//
//        @Override
//        public final void onOffsetChanged(AppBarLayout appBarLayout, int verticalOffset) {
//            if (verticalOffset == 0) {
//                if (mCurrentState != State.EXPANDED) {
//                    onStateChanged(appBarLayout, State.EXPANDED, verticalOffset);
//                }
//                mCurrentState = State.EXPANDED;
//            } else if (Math.abs(verticalOffset) >= appBarLayout.getTotalScrollRange()) {
//                if (mCurrentState != State.COLLAPSED) {
//                    onStateChanged(appBarLayout, State.COLLAPSED, verticalOffset);
//                }
//                mCurrentState = State.COLLAPSED;
//            } else {
//                onStateChanged(appBarLayout, State.IDLE, verticalOffset);
//                mCurrentState = State.IDLE;
//            }
//        }
//
//        public abstract void onStateChanged(AppBarLayout appBarLayout, State state, int verticalOffset);
//    }
//}
