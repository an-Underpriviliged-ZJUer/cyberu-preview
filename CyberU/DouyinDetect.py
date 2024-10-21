from CyberU import *
set_mode('detect')
from DouyinUtils import *


def sleep_for_ready2download_not_full():
    while ready_to_download.length() > max_ready():
        ready_to_download.refresh()
        log('下载队列已满。Detect 等待中...')
        sleep(10)

# RunMode()
# Exit()
def main():
    global host, page
    delog('douyin detect is starting ...')
    page = host = Chrome(
        # family='douyin_detect',
        mine=mine,
         # method='js',
        url='https://www.douyin.com/user/self',
    )
    sleep(2)
    while True:
        user_uid, author, urls=get_tasks(page)
        for video_url in urls:
            if not 'www.douyin.com' in video_url:
                video_url = 'https://www.douyin.com/'+video_url
            do(page=page, piece_page_url=video_url, author=author, filter=False, user_uid=user_uid)
            if parse_all_in_host:
                break
            sleep_for_ready2download_not_full()
            sleep(sleep_between_pieces())
        delete_var(name='douyin_last_detected')
        sleep(sleep_between_users())

if __name__ == '__main__':
    main()
