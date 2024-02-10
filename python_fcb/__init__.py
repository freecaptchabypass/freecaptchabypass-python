from .base import FCBClient
from pkg_resources import get_distribution, DistributionNotFound
from .tasks import (
    NoCaptchaTaskProxylessTask,
    RecaptchaV2TaskProxyless,
    NoCaptchaTask,
    RecaptchaV2Task,
    FunCaptchaProxylessTask,
    FunCaptchaTask,
    ImageToTextTask,
    RecaptchaV3TaskProxyless,
    HCaptchaTaskProxyless,
    HCaptchaTask,
    RecaptchaV2EnterpriseTaskProxyless,
    RecaptchaV2EnterpriseTask,
    GeeTestTaskProxyless,
    GeeTestTask,
    AntiGateTaskProxyless,
    AntiGateTask
)
from .exceptions import FCBException

AnticatpchaException = FCBException

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
