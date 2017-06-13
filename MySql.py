import pymysql

connect = pymysql.connect(
    user="root",
    password="root",
    port=3306,
    host="127.0.0.1",
    db="sprint_test",
    charset="utf8"
)


# 显示数据库版本
def showDbVersion():
    cursor = connect.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    connect.close()


# 创建表
def createTable():
    sql = """DROP TABLE IF EXISTS yt_instance; CREATE TABLE `yt_instance` (
  `id` bigint(20) NOT NULL,
  `chapter` int(11) DEFAULT NULL COMMENT '章节，用于剧情副本，表示属于不同的章',
  `numCur` int(11) DEFAULT NULL COMMENT '今日完成次数',
  `numAdd` int(11) DEFAULT NULL COMMENT '每日购买次数',
  `palyEffect` tinyint(4) DEFAULT NULL COMMENT '是否播放过特效',
  `passManual` tinyint(4) DEFAULT NULL COMMENT '是否手动通关过',
  `numMakeup` int(11) DEFAULT NULL COMMENT '累积补偿的次数, 第二天可以累积, 但是不能超过一定的上限',
  `numUseIn15dJSON` varchar(190) DEFAULT '{}' COMMENT '保存最近15天每天刷副本次数',
  `questReach` tinyint(4) DEFAULT NULL COMMENT '是否达成任务开启条件',
  `hideBossReach` tinyint(4) DEFAULT NULL COMMENT '是否达成隐藏boss开启条件',
  `numPassNoDropBase` varchar(190) DEFAULT '{}' COMMENT '通关但是没有掉落出保底物品的次数',
  `raidSuitNum` int(11) DEFAULT NULL COMMENT '本阶段团队副本已出套装数',
  `humanId` bigint(20) DEFAULT NULL COMMENT '所属用户',
  `levelReach` tinyint(4) DEFAULT NULL COMMENT '是否达成等级开启条件',
  `progress` varchar(190) DEFAULT '[]' COMMENT '副本进度',
  `prevReach` tinyint(4) DEFAULT NULL COMMENT '是否达成前置副本条件',
  `sn` int(11) DEFAULT NULL COMMENT '副本sn',
  `numEntered` int(11) DEFAULT NULL COMMENT '打过的次数',
  `raidNoSuitBossNum` int(11) DEFAULT NULL COMMENT '团队副本没有出套装的boss数',
  `numBuddyTask` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `yt_instance_humanId` (`humanId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
    cursor = connect.cursor()
    cursor.execute(sql)
    cursor.close()


# 插入表
def insertTable():
    sql = """INSERT INTO yt_instance(id,
         chapter)
         VALUES (2, 1)"""
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
    finally:
        cursor.close()

    print('成功插入', cursor.rowcount, '条数据')


# 查询表
def selectTable():
    sql = """SELECT * FROM yt_instance"""
    cursor = connect.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        chapter = row[1]
        print("id = %d chapter = %d " % (id, chapter))


# 更新表
def updateTable():
    sql = """UPDATE yt_instance SET chapter = 2 WHERE id = 1"""
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
    finally:
        cursor.close()

    print('成功更新', cursor.rowcount, '条数据')


# 删除表
def deleteTable():
    sql = """DELETE FROM yt_instance WHERE id = 1"""
    cursor = connect.cursor()
    try:
        cursor.execute(sql)
        connect.commit()
    except Exception as e:
        print(e)
        connect.rollback()
    finally:
        cursor.close()

    print('成功删除', cursor.rowcount, '条数据')


if __name__ == "__main__":
    deleteTable()
