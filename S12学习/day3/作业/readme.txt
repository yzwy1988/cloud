博客地址：http://blog.csdn.net/miniykyk/article/details/50633877

脚本：modify_ha.py
配置文件： haproxy.cfg
直接执行modify_ha.py文件即可。

    本代码实现了删除、增加和查看功能
    输出：
        1、获取ha记录
        2、增加ha记录
        3、删除ha记录
     
    如果用户输入的 1：
        然后输入：www.oldboy.org
        将配置文件 backend www.oldboy.org 节点下的所有记录获取到，并输入到终端
     
    如果用户输入的 2：
        并且输入如下信息： {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
        # 去配置文件中找到指定的节点：
        # backend test.oldboy.org
        # 如果已经存在，
            # 则在此节点下添加根据用输入构造出的记录，例如：
                server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
        # 如果不存在，
            # 则添加backend节点和记录，例如：
        backend test.oldboy.org
            server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
     
    如果用户输入的 3：
        并且输入如下信息：{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
        # 去配置文件中找到指定的节点，并删除指定记录，如：
        backend test.oldboy.org
             server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000
             server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000   # 删除掉
        # 如果backend下所有的记录都已经被删除，那么将当前 backend test.oldboy.org 也删除掉。

