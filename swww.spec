Name:           swww
Version:        0.4.3
Release:        1
URL:            https://github.com/Horus645/swww
Source0:        https://github.com/Horus645/swww/archive/refs/tags/v%{version}.tar.gz
Summary:        Efficient animated wallpaper daemon for Wayland, controlled at runtime.
License:        GPLv3
BuildRequires:  rustc
BuildRequires:  wlroots-dev
BuildRequires:  lz4-dev

 
%description
Efficient animated wallpaper daemon for Wayland, controlled at runtime.

%prep
%setup -q -n swww-%{version}
cargo fetch --locked


%build
export RUSTFLAGS="$RUSTFLAGS -C target-cpu=westmere -C target-feature=+avx -C opt-level=3"
cargo build --release --locked --offline


%install
install -D -m755 target/release/swww %{buildroot}/usr/bin/swww
install -m644 completions/swww.bash -pD %{buildroot}/usr/share/bash-completion/completions/swww.fish
install -m644 completions/swww.fish -pD %{buildroot}/usr/share/fish/vendor_completions.d/swww.fish

%files
%defattr(-,root,root,-)
/usr/bin/swww
/usr/share/bash-completion
/usr/share/fish
