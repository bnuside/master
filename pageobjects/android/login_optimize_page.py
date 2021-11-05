import os

from krunner.core.android.element import AndroidElement
from krunner.core.base import ImgElement


class LoginOptimizePage(object):
    """登录优化页面的元素"""

    curr_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'template')

    get_mobilephone_code = AndroidElement(text='获取验证码', annotation='获取验证码')
    email_icon = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/mail_login_view"]', annotation='邮箱icon')
    microblog_icon = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/sina_login_view"]',
                                    annotation='微博icon')
    retry_send_code = AndroidElement(text='重新发送', annotation='重新发送按钮')
    login_button = AndroidElement(text='登录', annotation='登录按钮')
    number_input_keyboard = ImgElement(template=curr_dir + '/number_input_keyboard.png', annotation='数字输入键盘')
    email_input_keyboard = ImgElement(template=curr_dir + '/email_input_keyboard.jpg', annotation='汉字输入键盘')
    phone_login_but = AndroidElement(text='手机号登录', annotation='手机号登录')
    agree_privacy_popup = AndroidElement(xpath='//*[@resource-id="com.smile.gifmaker:id/positive"]',annotation='同意隐私协议')
    phone_input_frame = AndroidElement(text='请输入手机号', annotation='输入手机号')