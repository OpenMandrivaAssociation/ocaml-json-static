Name:           ocaml-json-static
Version:        0.9.8
Release:        %mkrel 1
Summary:        OCaml JSON validator and converter (syntax extension)
License:        BSD
Group:          Development/Other
URL:            http://martin.jambon.free.fr/json-static.html
Source0:        http://martin.jambon.free.fr/json-static-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml >= 3.10.0
BuildRequires:  ocaml-findlib-devel
BuildRequires:  camlp4

# Make this dependency explicit because users won't be able
# to do much useful without it, and the automatic dependency
# checking script cannot pick it up.
Requires:       ocaml-json-wheel

%description
json-static is a tool for converting parsed JSON data with an
unchecked structure into specialized OCaml types and vice-versa.
It is a complement to the json-wheel library which provides a
parser and a (pretty-) printer.

%prep
%setup -q -n json-static-%{version}

%build
make

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README Changes yahoo.ml
%{_libdir}/ocaml/json-static

