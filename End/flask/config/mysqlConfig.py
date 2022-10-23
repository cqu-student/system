from properties.commonVar import LOCAL

def getMysqlConfig(env: object = LOCAL,serverName: object = '') -> object:
    #脚本运行以来的数据库配置
    if env == LOCAL:
        db_config = {
            'host':'127.0.0.1',
            'user':'root',
            'passwd':'12345678',
            'db':'db_platform',
            'prot':3306,
            'charset':'uft8'
        }
        return db_config