#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: e822d6e48dc0
#
Name     : libplacebo
Version  : 7.349.0
Release  : 82
URL      : https://github.com/haasn/libplacebo/archive/v7.349.0/libplacebo-7.349.0.tar.gz
Source0  : https://github.com/haasn/libplacebo/archive/v7.349.0/libplacebo-7.349.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.1 LGPL-2.1+
Requires: libplacebo-lib = %{version}-%{release}
Requires: libplacebo-license = %{version}-%{release}
BuildRequires : SDL2-dev
BuildRequires : SDL2_image-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-meson
BuildRequires : glslang-dev
BuildRequires : lcms2-dev
BuildRequires : llvm-dev
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libxxhash)
BuildRequires : pkgconfig(spirv-cross-c-shared)
BuildRequires : pypi(glad)
BuildRequires : pypi(mako)
BuildRequires : pypi-glad
BuildRequires : shaderc-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-build.patch

%description
# libplacebo
[![gitlab-ci badge](https://code.videolan.org/videolan/libplacebo/badges/master/pipeline.svg)](https://code.videolan.org/videolan/libplacebo/pipelines)
[![gitlab-ci coverage](https://code.videolan.org/videolan/libplacebo/badges/master/coverage.svg)](https://code.videolan.org/videolan/libplacebo/-/jobs/artifacts/master/file/coverage/index.html?job=test-gpu)
[![GitHub](https://img.shields.io/github/sponsors/haasn?logo=github)](https://github.com/sponsors/haasn)
[![PayPal](https://img.shields.io/badge/donate-PayPal-blue.svg?logo=paypal)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=SFJUTMPSZEAHC)
[![Patreon](https://img.shields.io/badge/pledge-Patreon-red.svg?logo=patreon)](https://www.patreon.com/haasn)

%package dev
Summary: dev components for the libplacebo package.
Group: Development
Requires: libplacebo-lib = %{version}-%{release}
Provides: libplacebo-devel = %{version}-%{release}
Requires: libplacebo = %{version}-%{release}

%description dev
dev components for the libplacebo package.


%package lib
Summary: lib components for the libplacebo package.
Group: Libraries
Requires: libplacebo-license = %{version}-%{release}

%description lib
lib components for the libplacebo package.


%package license
Summary: license components for the libplacebo package.
Group: Default

%description license
license components for the libplacebo package.


%prep
%setup -q -n libplacebo-7.349.0
cd %{_builddir}/libplacebo-7.349.0
%patch -P 1 -p1
pushd ..
cp -a libplacebo-7.349.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731429455
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=enabled \
-Ddemos=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dvulkan=enabled \
-Ddemos=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs
cd ../buildavx2;
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/libplacebo
cp %{_builddir}/libplacebo-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libplacebo/7fab4cd4eb7f499d60fe183607f046484acd6e2d || :
cp %{_builddir}/libplacebo-%{version}/demos/LICENSE %{buildroot}/usr/share/package-licenses/libplacebo/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libplacebo/cache.h
/usr/include/libplacebo/colorspace.h
/usr/include/libplacebo/common.h
/usr/include/libplacebo/config.h
/usr/include/libplacebo/d3d11.h
/usr/include/libplacebo/dispatch.h
/usr/include/libplacebo/dither.h
/usr/include/libplacebo/dummy.h
/usr/include/libplacebo/filters.h
/usr/include/libplacebo/gamut_mapping.h
/usr/include/libplacebo/gpu.h
/usr/include/libplacebo/log.h
/usr/include/libplacebo/opengl.h
/usr/include/libplacebo/options.h
/usr/include/libplacebo/renderer.h
/usr/include/libplacebo/shaders.h
/usr/include/libplacebo/shaders/colorspace.h
/usr/include/libplacebo/shaders/custom.h
/usr/include/libplacebo/shaders/deinterlacing.h
/usr/include/libplacebo/shaders/dithering.h
/usr/include/libplacebo/shaders/film_grain.h
/usr/include/libplacebo/shaders/icc.h
/usr/include/libplacebo/shaders/lut.h
/usr/include/libplacebo/shaders/sampling.h
/usr/include/libplacebo/swapchain.h
/usr/include/libplacebo/tone_mapping.h
/usr/include/libplacebo/utils/dav1d.h
/usr/include/libplacebo/utils/dav1d_internal.h
/usr/include/libplacebo/utils/dolbyvision.h
/usr/include/libplacebo/utils/frame_queue.h
/usr/include/libplacebo/utils/libav.h
/usr/include/libplacebo/utils/libav_internal.h
/usr/include/libplacebo/utils/upload.h
/usr/include/libplacebo/vulkan.h
/usr/lib64/libplacebo.so
/usr/lib64/pkgconfig/libplacebo.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libplacebo.so.349
/usr/lib64/libplacebo.so.349

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libplacebo/7fab4cd4eb7f499d60fe183607f046484acd6e2d
/usr/share/package-licenses/libplacebo/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
