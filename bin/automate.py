import git
repo = git.Repo( '/var/www/html/python/shit')
print repo.git.status()
# checkout and track a remote branch
print repo.git.checkout( 'master' )
# add a file
print repo.git.add( '/var/www/html/python/shit/bin/finaltest.py' )
# commit
print repo.git.commit( m='my commit message' )


repo.git.push()
# now we are one commit ahead
print repo.git.status()
# now push
