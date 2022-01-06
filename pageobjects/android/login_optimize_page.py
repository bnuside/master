import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class LoginOptimizePage(object):
    """主站登录优化页面的元素"""
    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    get_mobilephone_code = AndroidElement(text='获取验证码', annotation='获取验证码')
    smile_email_icon = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/mail_login_view"]', annotation='邮箱icon')
    smile_microblog_icon = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/sina_login_view"]',
                                    annotation='微博icon')
    retry_send_code = AndroidElement(text='重新发送', annotation='重新发送按钮')
    login_button = AndroidElement(text='登录', annotation='登录按钮')
    number_input_keyboard = ImgElement(template=curr_dir + '/number_input_keyboard.png', annotation='数字输入键盘')
    email_input_keyboard = ImgElement(template=curr_dir + '/email_input_keyboard.jpg', annotation='汉字输入键盘')
    phone_login_but = AndroidElement(text='手机号登录', annotation='手机号登录')
    smile_agree_privacy_popup = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/positive"]',
                                         annotation='同意隐私协议')
    phone_input_frame = AndroidElement(text='请输入手机号', annotation='输入手机号')
    smile_pwd_input_but = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/user_phone_num_info"]',
                                   annotation='密码输入框')
    pwd_regist_but = AndroidElement(text='密码登录', annotation='密码登录按钮')
    smile_privacy_agreement_but = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/protocol_checkbox"]',
                                           annotation='同意隐私文案')
    smile_first_account_photo = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/icon_one"]',
                                         annotation='第一个登录头像')
    smile_second_account_photo = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/icon_two"]',
                                          annotation='第二个登录头像')

