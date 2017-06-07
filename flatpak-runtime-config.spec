Name:           flatpak-runtime-config
Version:        26
Release:        1%{?dist}
Summary:        Configuration files that live inside the flatpak runtime
Source1:        50-xdg-app.conf
BuildArch:      noarch

License:        GPL


%description
Configuration files that live inside the flatpak runtime

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
%{_sysconfdir}/ld.so.conf.d/app.conf

%changelog
* Wed Jun  7 2017 Owen Taylor <otaylor@redhat.com>
- Strip down to just config files

* Wed Jun  3 2015 Alexander Larsson <alexl@redhat.com>
- Initial version
