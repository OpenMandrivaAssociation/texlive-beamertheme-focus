Name:		texlive-beamertheme-focus
Version:	69742
Release:	1
Summary:	A minimalist presentation theme for LaTeX Beamer
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-focus
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-focus.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-focus.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A presentation theme for LaTeX Beamer that aims at a clean and
minimalist design, so to minimize distractions and put the
focus directly on the content.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-focus
%doc %{_texmfdistdir}/doc/latex/beamertheme-focus

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
