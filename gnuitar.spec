Summary:	Guitar effects processor
Summary(pl):	Procesor efektów gitarowych
Name:		gnuitar
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/gnuitar/%{name}-%{version}.tar.bz2
# Source0-md5:	8b8375f879191c6c35bd30160f158d7c
Patch0:		%{name}-am.patch
URL:		http://ns2.ziet.zhitomir.ua/~fonin/downloads.php#gnuitar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel

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

%description -l pl
GNUitar pozwala zamieniæ komputer z rozbudowany procesor d¼wiêku i
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
Summary(pl):	Procesor efektów gitarowych - efekt distort2
Group:		X11/Applications/Sound
Requires:	gnuitar

%description distort2
Lookup tables for distort2 effect of GNUitar.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=${RPM_BUILD_ROOT}

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/gnuitar
rm -f $RPM_BUILD_ROOT%{_datadir}/gnuitar/distort2lookup_*

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/gnuitar

%files distort2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gen_distort2_lookup
%dir %{_datadir}/gnuitar
%dir %{_datadir}/gnuitar/distort2
%{_datadir}/gnuitar/distort2/*
