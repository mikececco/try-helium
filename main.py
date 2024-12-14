from helium import *

start_chrome('google.com')
write('helium selenium github')
press(ENTER)
wait_until(Text('mherrmann/helium').exists)
click('mherrmann/helium')
go_to('github.com/login')
write('username', into='Username')
write('password', into='Password')
click('Sign in')
kill_browser()