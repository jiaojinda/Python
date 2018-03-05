import os
import time
# 1. 需要备份的文件与 目 录将被
# 指定在一个列 表中 。
# 例 如在 Windows 下：
# source = [' "C: \\My Documents"' , ' C: \\Code' ]
# 又例如在 Mac OS X 与 Linux 下：
source = ['G:\\python\\backupTest\\source' ]
# 在这里要注意到 我们 必须 在字符串 中 使用 双引 号
# 用 以括起其中 包含空格的名 称。
# 2. 备份文件必须 存储在一个
# 主备份目 录中
# 例 如在 Windows 下：
# target_dir = ' E: \\Backup'
# 又例如在 Mac OS X 和 Linux 下：
target_dir = 'G:\\python\\backupTest\\backup'
# 要记得将这里的目 录地址修改至你将使用 的路径
# 如果目 标目 录还不存在， 则 进行创 建
if not os. path. exists( target_dir) :
    os. mkdir( target_dir) # 创 建目 录
# 3. 备份文件将打包压 缩成 zip 文件。
# 4. 将当 前日 期作为 主备份目 录下的
# 子目 录名 称
today = target_dir + os. sep + time. strftime( '%Y%m%d' )
# 将当 前时间 作为 zip 文件的文件名
now = time. strftime( '%H%M%S' )
# 添加一条来自 用 户 的注释以创 建
# zip 文件的文件名
comment = input( 'Enter a comment --> ' )
# 检查是否有评论键入
if len( comment) == 0:
    target = today + os. sep + now + '.zip'
else:
    target = today + os. sep + now + '_' + comment. replace( ' ' , '_' ) + '.zip'
# 如果子目 录尚不存在则 创 建一个
if not os. path. exists( today) :
    os. mkdir( today)
print( 'Successfully created directory' , today)
# 5. 我们 使用 zip 命令将文件打包成 zip 格式
zip_command = "zip -r {0} {1}". format( target,
                                            ' ' . join( source) )
# 运行备份
print( 'Zip command is: ' )
print( zip_command)
print( 'Running: ' )
if os. system( zip_command) == 0:
    print( ' Successful backup to' , target)
else:
    print( ' Backup FAILED' )
