<h1 align="center">Pexels-Crawler</h1>
<p align="center">Pexels-Crawler is a efficient web crawler to get pictures from the <a href="https://www.pexels.com/">PEXELS</a> . It is totally handcarfted, with love.</p>

[![Python](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/community/)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)
## Installation

Get pexels-crawler from GitHub. There are several variants to do it:

### Download [latest master branch][download-latest-url].

   [![git-image]][git-url]

   ```sh
   $ git clone https://github.com/Zach-Leo/pexels-crawler
   ```

   Clone command will give you the **whole repository**. 

## Configuration

pexels-crawler comes with few configurations.
```sh
   $ vim config.yaml
   ```

```yaml

#Http Header (for the most time, you don't need to change it)
user_agent: 'Mozilla/5.0 AppleWebKit/537.36 Chrome/65.0.3325.181 Safari/537.36'

#Where you want to download
download_dir: '/users/haohao/Desktop/pexels/'

#The content you need
element: 'cat'

#The number of pages you want to get
search_range: 20

```

## Usage

   ```sh
   $ python crawler.py
   ```


## Contributing

Contribution is welcome, feel free to open an issue and fork. Waiting for your pull request.

[git-image]: https://img.shields.io/badge/install%20with%20-git-blue.svg
[curl-tar-image]: https://img.shields.io/badge/install%20with%20-curl%20%7C%20tar-blue.svg
[curl-tar-wget-image]: https://img.shields.io/badge/install%20with%20-curl%20%7C%20tar%20%7C%20wget-blue.svg
[git-url]: http://lmgtfy.com/?q=linux+git+install
[curl-tar-url]: http://lmgtfy.com/?q=linux+curl+tar+install
[curl-tar-wget-url]: http://lmgtfy.com/?q=linux+curl+tar+wget+install

[python]: https://img.shields.io/badge/python-3.6-blue.svg
[license]: https://img.shields.io/github/license/mashape/apistatus.svg



[download-latest-url]: https://github.com/Zach-Leo/pexels-crawler/archive/master.zip


