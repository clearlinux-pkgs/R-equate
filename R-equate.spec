#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-equate
Version  : 2.0.7
Release  : 11
URL      : https://cran.r-project.org/src/contrib/equate_2.0.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/equate_2.0.7.tar.gz
Summary  : Observed-Score Linking and Equating
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
and equating under the single-group, equivalent-groups,
  and nonequivalent-groups with anchor test(s) designs.
  Equating types include identity, mean, linear, general
  linear, equipercentile, circle-arc, and composites of
  these. Equating methods include synthetic, nominal
  weights, Tucker, Levine observed score, Levine true
  score, Braun/Holland, frequency estimation, and chained
  equating. Plotting and summary methods, and methods for
  multivariate presmoothing and bootstrap error estimation
  are also provided.

%prep
%setup -q -c -n equate

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552920646

%install
export SOURCE_DATE_EPOCH=1552920646
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library equate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library equate
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library equate
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  equate || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/equate/CITATION
/usr/lib64/R/library/equate/DESCRIPTION
/usr/lib64/R/library/equate/INDEX
/usr/lib64/R/library/equate/Meta/Rd.rds
/usr/lib64/R/library/equate/Meta/data.rds
/usr/lib64/R/library/equate/Meta/features.rds
/usr/lib64/R/library/equate/Meta/hsearch.rds
/usr/lib64/R/library/equate/Meta/links.rds
/usr/lib64/R/library/equate/Meta/nsInfo.rds
/usr/lib64/R/library/equate/Meta/package.rds
/usr/lib64/R/library/equate/Meta/vignette.rds
/usr/lib64/R/library/equate/NAMESPACE
/usr/lib64/R/library/equate/NEWS
/usr/lib64/R/library/equate/NEWS.md
/usr/lib64/R/library/equate/R/equate
/usr/lib64/R/library/equate/R/equate.rdb
/usr/lib64/R/library/equate/R/equate.rdx
/usr/lib64/R/library/equate/data/Rdata.rdb
/usr/lib64/R/library/equate/data/Rdata.rds
/usr/lib64/R/library/equate/data/Rdata.rdx
/usr/lib64/R/library/equate/doc/equate-jss.R
/usr/lib64/R/library/equate/doc/equate-jss.Rnw
/usr/lib64/R/library/equate/doc/equate-jss.pdf
/usr/lib64/R/library/equate/doc/index.html
/usr/lib64/R/library/equate/help/AnIndex
/usr/lib64/R/library/equate/help/aliases.rds
/usr/lib64/R/library/equate/help/equate.rdb
/usr/lib64/R/library/equate/help/equate.rdx
/usr/lib64/R/library/equate/help/paths.rds
/usr/lib64/R/library/equate/html/00Index.html
/usr/lib64/R/library/equate/html/R.css
