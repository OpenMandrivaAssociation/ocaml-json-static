%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	OCaml JSON validator and converter (syntax extension)
Name:		ocaml-json-static
Version:	0.9.8
Release:	3
License:	BSD
Group:		Development/Other
Url:		http://martin.jambon.free.fr/json-static.html
Source0:	http://martin.jambon.free.fr/json-static-%{version}.tar.bz2
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib-devel
# Make this dependency explicit because users won't be able
# to do much useful without it, and the automatic dependency
# checking script cannot pick it up.
Requires:	ocaml-json-wheel

%description
json-static is a tool for converting parsed JSON data with an
unchecked structure into specialized OCaml types and vice-versa.
It is a complement to the json-wheel library which provides a
parser and a (pretty-) printer.

%files
%doc LICENSE README Changes yahoo.ml
%{_libdir}/ocaml/json-static

#----------------------------------------------------------------------------

%prep
%setup -q -n json-static-%{version}

%build
make

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

