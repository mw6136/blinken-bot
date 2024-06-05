# Sample script to listen to Antony Blinken's top songs on his Spotify page (to pump up his numbers)

# RPA for Python's simple and powerful API for robotic process automation (RPA)
# pip install rpa to install, pip install rpa --upgrade to get latest version

# to use in Jupyter notebook, Python script or interactive shell
import rpa as r

# use init() to start TagUI, it auto downloads TagUI on first run
# default init(visual_automation = False, chrome_browser = True)
r.init()

# use url('your_url') to go to web page, url() returns current URL
r.url('https://open.spotify.com/artist/5ZWgy4Riyzr0QtvcIKiZmF')

# use type() to enter text into an UI element or x, y location
# '[enter]' = enter key, '[clear]' = clear field
r.type('ybar-sbq', 'github')

# use read() to fetch and return text from UI element
search_text = r.read('ybar-sbq')
print(search_text)

# use click() to click on an UI element or x, y location
# rclick() = right-click, dclick() = double-click
r.click('ybar-search')

# use wait() to wait for a number of seconds
# default wait() is 5 seconds
r.wait(6.6)

# use snap() to save screenshot of page or UI element
# page = web page, page.png = computer screen
r.snap('page', 'results.png')
r.snap('logo', 'logo.png')

# another example of interacting with a web page
# include http:// or https:// in URL parameter
r.url('https://open.spotify.com/artist/5ZWgy4Riyzr0QtvcIKiZmF')
r.type('//*[@name="q"]', 'Top Song listen.')
r.snap('page', 'blinken_spotify.png')
r.wait(4.4)

# use close() to close TagUI process and web browser
# if you forget to close, just close() next time
r.close()