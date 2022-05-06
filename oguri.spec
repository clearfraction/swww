Name     : oguri
Version  : 6937fee10a9b0ef3ad8f94f606c0e0d9e7dec564
Release  : 1
URL      : https://github.com/vilhalmer/oguri
Source0  : https://github.com/vilhalmer/oguri/archive/master.tar.gz
Summary : A very nice animated wallpaper daemon for Wayland compositors
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-meson
BuildRequires : cairo-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)


%description
A very nice animated wallpaper daemon for Wayland compositors.


%prep
%setup -q -n oguri-master

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1646879499
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/bin/oguri
/usr/bin/ogurictl
