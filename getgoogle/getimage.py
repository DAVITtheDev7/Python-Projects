from icrawler.builtin import GoogleImageCrawler

def google_img_downloader():

    crawler = GoogleImageCrawler(storage = {'root_dir':'images'})
    word = input("\nEnter anything: ")
    n = int(input("How many images do you want? "))
    crawler.crawl(keyword = word,max_num = n)

def main():
    google_img_downloader()

while True:
    if __name__ == '__main__':
            main()

