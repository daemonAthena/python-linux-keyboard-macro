# Maintainer: daemonAthena <daemonAthena@gmail.com>
pkgname='python-linux-keyboard-macro' 
pkgver=1
pkgrel=1 # Only make this an integer
pkgdesc="The first of many presents to my girlfriend"
arch=('x86_64')
url="https://github.com/daemonAthena/python-linux-keyboard-macro"
license=('MIT')
depends=('python>=3.14.7') # keyboard and os should come installed with python
makedepends=('git' 'python-keyboard')
install= #optional post and pretransactional hooks points to a .install file
source=('python-linux-keyboard-macro::git+https://github.com/daemonAthena/python-linux-keyboard-macro.git')
sha256sums=('SKIP')

pkgver(){
	cd "$pkgname"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	install -Dm755 ./keyboard_macro.py "$pkgdir/usr/bin/keyboard-macro"
}
