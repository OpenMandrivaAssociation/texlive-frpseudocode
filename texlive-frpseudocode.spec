Name:		texlive-frpseudocode
Version:	56088
Release:	2
Summary:	French translation for the algorithmicx package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/frpseudocode
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frpseudocode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/frpseudocode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is intended for use alongside Szasz Janos'
algorithmicx package. Its aim is to provide a French
translation of terms and words used in algorithms to make it
integrate seamlessly in a French written document.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/frpseudocode
%doc %{_texmfdistdir}/doc/latex/frpseudocode

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
