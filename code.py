from psdi.iface.mic import MicService
from psdi.server import MXServer

micService = MXServer.getMXServer().lookup("MIC");
userInfo = micService.getNewUserInfo();

# queueName can be derived from any common maxvars property as well
queueName = 'jms/maximo/int/queues/sqout';

micService.processJMSRecovery(queueName, userInfo);