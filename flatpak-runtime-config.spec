Name:           flatpak-runtime-config
Version:        27
Release:        1%{?dist}
Summary:        Configuration files that live inside the flatpak runtime
Source1:        50-xdg-app.conf
BuildArch:      noarch

License:        GPL

%description
This package includes configuration files that are installed into the flatpak
runtime filesystem during the runtime creation process; it is also installed
into the build root when building RPMs. It contains all configuration
files that need to be different when executing a flatpak.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_prefix}/cache/fontconfig
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d
install -t $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d -m 644 %{SOURCE1} 

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/
echo "/app/%{_lib}" > $RPM_BUILD_ROOT%{_sysconfdir}/ld.so.conf.d/app.conf

%post -p /sbin/ldconfig

%files
%{_prefix}/cache/fontconfig
%{_sysconfdir}/fonts/conf.d/*
# Note that this is necessary at build time but has no effect during flatpak
# execution, since /etc/ld.so.cache will only contain the libraries from
# the runtime and not any libraries that are separately mounted in /app/lib[64].
# During flatpak execution LD_LIBRARY_PATH is used to find the libraries from
# /app/lib[64].
%{_sysconfdir}/ld.so.conf.d/app.conf

%changelog
* Wed Jun  7 2017 Owen Taylor <otaylor@redhat.com>
- Strip down to just config files

* Wed Jun  3 2015 Alexander Larsson <alexl@redhat.com>
- Initial version
