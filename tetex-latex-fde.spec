# TODO:
# - check proper version
%define short_name fde
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;
Summary:	Formats for International Journal Functional Differential Equations
Summary(pl.UTF-8):	Formaty dla publikujących w Functional Differential Equations
Name:		tetex-latex-%{short_name}
Version:	1.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://www.hait.ac.il/staff/benzionS/FDE/Makros.zip
# Source0-md5:	e908f231f37895bf8961a453e8bff837
Source1:	http://www.hait.ac.il/staff/benzionS/FDE/Example.zip
# Source1-md5:	0b1c2c25b9703830f3fed798d9bf9a39
BuildRequires:	unzip
Requires:	tetex-latex
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Functional Differential Equations (FDE) is devoted to the publication
of high quality mathematical papers in the area of functional
differential equations. Emphasis will be placed on important
developments in abstract and applied FDE involving Boundary Value
Problems, Stability Theory, Oscillation Theory, Variational Problems,
Optimization Theory and Control Theory. Papers on Functional
Differential Equations with Impulses, Integral Equations, some related
questions. Partial Differential Equations, Ordinary Differential
Equations and Difference Equations are also welcome by the journal.
FDE will also support the publication of serious, comprehensive and
authoritative survey articles aiming at informing our readers of the
recent developments as well as the historical background of the
relevant subjects.

To publish in that journal you need these styles.

%description -l pl.UTF-8
Functional Differential Equations (FDE) to pismo przeznaczone do
publikowania wysokiej jakości artykułów matematycznych z zakresu
funkcyjnych równań różniczkowych. Nacisk jest położony na ważne
postępy w abstrakcyjnych i stosowanych funkcyjnych równaniach
różniczkowych związanych z problemami wartości granicznych, teorią
stabilności, teorią oscylacji, problemami wariacyjnymi, teorią
optymalizacji i teorią sterowania. Artykuły dotyczące funkcyjnych
równań różniczkowych z impulsami, równaniami całkowymi i niektórymi
związanymi problemami. Cząstkowe równania różniczkowe, zwykłe
równania różniczkowe i równania różnicowe są również mile widziane w
tym piśmie. FDE wspiera także publikowanie poważnych, obszernych i
autorytatywnych artykułów przeglądowych, których celem jest
informowanie czytelników o ostatnich postępach, a także tle
historycznym związanym z tymi tematami.

Style z tego pakietu są potrzebne do publikowania w tym piśmie.

%prep
%setup -q -c
unzip -n %{SOURCE1} -d examples

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install *.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc examples/*.tex
%dir %{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/tex/latex/%{short_name}/*.sty
