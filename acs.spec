Summary:	Spice-like analog simulator
Summary(pl):	Symulator uk³adów analogowych typu Spice
Name:		acs
Version:	0.29
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://metalab.unc.edu/pub/Linux/apps/circuits/%{name}-%{version}.tar.gz
Patch0:		%{name}-opt.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ACS is a general purpose circuit simulator. It performs nonlinear dc
and transient analyses, fourier analysis, and ac analysis linearized
at an operating point. It is fully interactive and command driven. It
can also be run in batch mode or as a server. The output is produced
as it simulates. Spice compatible models for the MOSFET (level
1,2,3,6) and diode are included in this release.

%description -l pl
ACS jest symulatorem obwodów elektronicznych. Umo¿liwia on analizy:
nieliniow± dc, analizy przej¶ciowe, analizy fouriera oraz analizy ac
zlinearyzowane w czasie operacji. Symulator jest w pe³ni interaktywny
ale mo¿e byæ uruchamiany w trybie batch lub serwer. Modele MOSFET
(poziom 1,2,3,6) oraz diod kompatybilne ze Spice s± zawarte w
pakiecie.

%prep
%setup -q
%patch0 -p1

%build
OPT_FLAGS="%{rpmcflags}"; export OPT_FLAGS
cd src
%{__make} linux

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

install src/LINUX/acs	$RPM_BUILD_ROOT%{_bindir}/
install examples/*	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc man/man doc/{acs-tutorial,whatisit,history,relnotes.029}
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
