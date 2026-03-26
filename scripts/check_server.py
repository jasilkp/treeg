import urllib.request

def main():
    try:
        resp = urllib.request.urlopen('http://127.0.0.1:8000/', timeout=5)
        print('STATUS', resp.getcode())
        print(resp.read(600).decode('utf-8', errors='replace')[:1000])
    except Exception as e:
        print('ERROR', repr(e))

if __name__ == '__main__':
    main()
