import sys
import pathlib

from loguru import logger

# Path setting
relative_directory = pathlib.Path(__file__).parent.parent  # Garuda code relative path
result_save_dir = relative_directory.joinpath('results')  # Result save directory
log_path = result_save_dir.joinpath('garuda.log')  # Garuda log save path

# Log configuration
# Terminal log output format
stdout_fmt = '<cyan>{time:HH:mm:ss,SSS}</cyan> ' \
             '[<level>{level: <5}</level>] ' \
             '<blue>{module}</blue>:<cyan>{line}</cyan> - ' \
             '<level>{message}</level>'
# Log file record format
logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
              '[<level>{level: <5}</level>] ' \
              '<cyan>{process.name}({process.id})</cyan>:' \
              '<cyan>{thread.name: <18}({thread.id: <5})</cyan> | ' \
              '<blue>{module}</blue>.<blue>{function}</blue>:' \
              '<blue>{line}</blue> - <level>{message}</level>'

logger.remove()
logger.level(name='TRACE', color='<cyan><bold>', icon='✏️')
logger.level(name='DEBUG', color='<blue><bold>', icon='🐞 ')
logger.level(name='INFOR', no=20, color='<green><bold>', icon='ℹ️')
logger.level(name='QUITE', no=25, color='<green><bold>', icon='🤫 ')
logger.level(name='ALERT', no=30, color='<yellow><bold>', icon='⚠️')
logger.level(name='ERROR', color='<red><bold>', icon='❌️')
logger.level(name='FATAL', no=50, color='<RED><bold>', icon='☠️')

# If you want to run OneForAll silently in the command terminal, you can set the level in the following line to QUITE
# The command terminal log level defaults to INFOR
logger.add(sys.stderr, level='INFOR', format=stdout_fmt, enqueue=True)
# The default log file level is DEBUG
logger.add(log_path, level='DEBUG', format=logfile_fmt, enqueue=True, encoding='utf-8')
