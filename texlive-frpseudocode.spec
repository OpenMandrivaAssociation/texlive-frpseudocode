%global tl_name frpseudocode
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3.0
Release:	%{tl_revision}.1
Summary:	French translation for the algorithmicx package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/frpseudocode
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frpseudocode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frpseudocode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is intended for use alongside Szasz Janos' algorithmicx
package. Its aim is to provide a French translation of terms and words
used in algorithms to make it integrate seamlessly in a French written
document.

