Summary:	Guitar effects processor
Summary(pl.UTF-8):   Procesor efektów gitarowych
Name:		gnuitar
Version:	0.3.1
Release:	3
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
# Source0-md5:	8b8375f879191c6c35bd30160f158d7c
Patch0:		%{name}-am.patch
#http://ns2.ziet.zhitomir.ua/~fonin/projects/gnuitar/patches/patch-0.3.1-1
Patch1:		%{name}-patch-0.3.1-1.patch
#http://ns2.ziet.zhitomir.ua/~fonin/projects/gnuitar/patches/patch-0.3.1-2
Patch2:		%{name}-patch-0.3.1-2.patch
URL:		http://ns2.ziet.zhitomir.ua/~fonin/downloads.php#gnuitar
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a guitar effects software that allows you to use your computer
as powerful guitar processor. Includes effects:
- wah-wah
- sustain
- two flavours of distortion
- reverberator, echo, delay
- tremolo
- vibrato
- chorus/flanger
- phasor
- noise gate

%description -l pl.UTF-8
GNUitar pozwala zamienić komputer z rozbudowany procesor dźwięku i
efektów gitarowych. Wbudowane efekty:
- wah-wah (tzw. kaczka)
- sustain
- distortion w dwóch rodzajach (tzw. przester)
- reverberator, echo, delay
- tremolo
- vibrato
- chorus/flanger
- phasor
- noise gate

%package distort2
Summary:	Guitar effects processor - distort2 effect
Summary(pl.UTF-8):   Procesor efektów gitarowych - efekt distort2
Group:		X11/Applications/Sound
Requires:	%{name}

%description distort2
Lookup tables for distort2 effect of GNUitar.

%description distort2 -l pl.UTF-8
Tablice dla efektu GNUitar distort2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=${RPM_BUILD_ROOT}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name}.ico $RPM_BUILD_ROOT%{_pixmapsdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnuitar
rm -f $RPM_BUILD_ROOT%{_datadir}/gnuitar/distort2lookup_*
rm -rf $RPM_BUILD_ROOT%{_datadir}/gnuitar/win32

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gnuitar
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.ico

%files distort2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gen_distort2_lookup
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/distort2
%{_datadir}/%{name}/distort2/*
