Name:           libxcb
Version:        1.9
Release:        0
License:        MIT
Summary:        X11 core protocol C library
Url:            http://xcb.freedesktop.org/
Group:          Graphics & UI Framework/Libraries

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libxcb.manifest
BuildRequires:  pkgconfig
BuildRequires:  python >= 2.6
BuildRequires:  python-xml
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(pthread-stubs)
BuildRequires:  pkgconfig(xau) >= 0.99.2
BuildRequires:  pkgconfig(xcb-proto) >= 1.7

%description
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-composite
Summary:        X11 Composite Extension C library

%description -n libxcb-composite
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The Composite extension causes a entire sub-tree of the window
hierarchy to be rendered to an off-screen buffer. Applications can
then take the contents of that buffer and do whatever they like. The
off-screen buffer can be automatically merged into the parent window
or merged by external programs, called compositing managers.

%package -n libxcb-damage
Summary:        X11 Damage Extension C library

%description -n libxcb-damage
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Damage Extension allows applications to track modified regions
of drawables.

%package -n libxcb-dpms
Summary:        X11 DPMS Extension C library

%description -n libxcb-dpms
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-dri2
Summary:        X11 DRI2 Extension C library

%description -n libxcb-dri2
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-glx
Summary:        X11 GLX Extension C library

%description -n libxcb-glx
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-randr
Summary:        X11 RandR Extension C library

%description -n libxcb-randr
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Resize, Rotate and Reflect Extension (RandR) allows clients to
dynamically change X screens, so as to resize, to change the
orientation and layout of the root window of a screen.

%package -n libxcb-record
Summary:        X11 RECORD Extension C library

%description -n libxcb-record
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The RECORD extension supports the recording and reporting of all core
X protocol and arbitrary X extension protocol.

%package -n libxcb-render
Summary:        X11 Render Extension C library

%description -n libxcb-render
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-res
Summary:        X11 Resource Extension C library

%description -n libxcb-res
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-screensaver
Summary:        X11 ScreenSaver Extension C library

%description -n libxcb-screensaver
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package -n libxcb-shape
Summary:        X11 Shape Extension C library

%description -n libxcb-shape
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

- X11 Nonrectangular Window Shape extension (Xshape)

%package -n libxcb-shm
Summary:        X11 Shared Memory Extension C library

%description -n libxcb-shm
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The MIT Shared Memory (MIT-SHM) Extension allows exchanging image
data between client and server using shared memory, so that it does
not need to be transferred over sockets.

%package -n libxcb-sync
Summary:        X11 Sync Extension C library

%description -n libxcb-sync
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-xevie
Summary:        X11 Xevie Extension C library

%description -n libxcb-xevie
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The EvIE (Event Interception Extension) allows for clients to be able
to intercept all events coming through the server and then decide
what to do with them, including being able to modify or discard
events.

%package -n libxcb-xf86dri
Summary:        X11 XFree86-DRI Extension C library

%description -n libxcb-xf86dri
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

%package -n libxcb-xfixes
Summary:        X11 Xfixes Extension C library

%description -n libxcb-xfixes
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Fixes extension provides applications with work-arounds for
various limitations in the core protocol.

%package -n libxcb-xinerama
Summary:        X11 Xinerama Extension C library

%description -n libxcb-xinerama
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

Xinerama is an extension to the X Window System which enables
multi-headed X applications and window managers to use two or more
physical displays as one large virtual display.

%package -n libxcb-xprint
Summary:        X11 XPrint Extension C library

%description -n libxcb-xprint
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

libxcb-xprint provides APIs to allow client applications to render to
non-display devices.

%package -n libxcb-xtest
Summary:        X11 XTEST Extension C library

%description -n libxcb-xtest
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The XTEST extension is a minimal set of client and server extensions
required to completely test the X11 server with no user intervention.
This extension is not intended to support general journaling and
playback of user actions.

%package -n libxcb-xv
Summary:        X11 video Extension C library

%description -n libxcb-xv
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

The X Video Extension (Xv) extension provides support for video
adaptors attached to an X display. It takes the approach that a
display may have one or more video adaptors, each of which has one or
more ports through which independent video streams pass.

%package -n libxcb-xvmc
Summary:        X11 Video Motion Compensation Extension C library

%description -n libxcb-xvmc
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

X-Video Motion Compensation (XvMC), is an extension of the X video
extension (Xv) for the X Window System. The XvMC API allows video
programs to offload portions of the video decoding process to the GPU
video-hardware.

%package devel
Summary:        Development files for the X11 protocol C library
Requires:       libxcb-composite = %{version}
Requires:       libxcb-damage = %{version}
Requires:       libxcb-dpms = %{version}
Requires:       libxcb-dri2 = %{version}
Requires:       libxcb-glx = %{version}
Requires:       libxcb-randr = %{version}
Requires:       libxcb-record = %{version}
Requires:       libxcb-render = %{version}
Requires:       libxcb-res = %{version}
Requires:       libxcb-screensaver = %{version}
Requires:       libxcb-shape = %{version}
Requires:       libxcb-shm = %{version}
Requires:       libxcb-sync = %{version}
Requires:       libxcb-xevie = %{version}
Requires:       libxcb-xf86dri = %{version}
Requires:       libxcb-xfixes = %{version}
Requires:       libxcb-xinerama = %{version}
Requires:       libxcb-xprint = %{version}
Requires:       libxcb-xtest = %{version}
Requires:       libxcb-xv = %{version}
Requires:       libxcb-xvmc = %{version}

%description devel
The X protocol C-language Binding (XCB) is a replacement for Xlib
featuring a small footprint, latency hiding, direct access to the
protocol, improved threading support, and extensibility.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%autogen
%configure --docdir=%_docdir/%{name} --disable-static
make %{?_smp_mflags}

%install
%make_install

%post   -n libxcb -p /sbin/ldconfig

%postun -n libxcb -p /sbin/ldconfig

%post   -n libxcb-composite -p /sbin/ldconfig

%postun -n libxcb-composite -p /sbin/ldconfig

%post   -n libxcb-damage -p /sbin/ldconfig

%postun -n libxcb-damage -p /sbin/ldconfig

%post   -n libxcb-dpms -p /sbin/ldconfig

%postun -n libxcb-dpms -p /sbin/ldconfig

%post   -n libxcb-dri2 -p /sbin/ldconfig

%postun -n libxcb-dri2 -p /sbin/ldconfig

%post   -n libxcb-glx -p /sbin/ldconfig

%postun -n libxcb-glx -p /sbin/ldconfig

%post   -n libxcb-randr -p /sbin/ldconfig

%postun -n libxcb-randr -p /sbin/ldconfig

%post   -n libxcb-record -p /sbin/ldconfig

%postun -n libxcb-record -p /sbin/ldconfig

%post   -n libxcb-render -p /sbin/ldconfig

%postun -n libxcb-render -p /sbin/ldconfig

%post   -n libxcb-res -p /sbin/ldconfig

%postun -n libxcb-res -p /sbin/ldconfig

%post   -n libxcb-screensaver -p /sbin/ldconfig

%postun -n libxcb-screensaver -p /sbin/ldconfig

%post   -n libxcb-shape -p /sbin/ldconfig

%postun -n libxcb-shape -p /sbin/ldconfig

%post   -n libxcb-shm -p /sbin/ldconfig

%postun -n libxcb-shm -p /sbin/ldconfig

%post   -n libxcb-sync -p /sbin/ldconfig

%postun -n libxcb-sync -p /sbin/ldconfig

%post   -n libxcb-xevie -p /sbin/ldconfig

%postun -n libxcb-xevie -p /sbin/ldconfig

%post   -n libxcb-xf86dri -p /sbin/ldconfig

%postun -n libxcb-xf86dri -p /sbin/ldconfig

%post   -n libxcb-xfixes -p /sbin/ldconfig

%postun -n libxcb-xfixes -p /sbin/ldconfig

%post   -n libxcb-xinerama -p /sbin/ldconfig

%postun -n libxcb-xinerama -p /sbin/ldconfig

%post   -n libxcb-xprint -p /sbin/ldconfig

%postun -n libxcb-xprint -p /sbin/ldconfig

%post   -n libxcb-xtest -p /sbin/ldconfig

%postun -n libxcb-xtest -p /sbin/ldconfig

%post   -n libxcb-xv -p /sbin/ldconfig

%postun -n libxcb-xv -p /sbin/ldconfig

%post   -n libxcb-xvmc -p /sbin/ldconfig

%postun -n libxcb-xvmc -p /sbin/ldconfig

%files -n libxcb
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb.so.1*

%files -n libxcb-composite
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-composite.so.0*

%files -n libxcb-damage
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-damage.so.0*

%files -n libxcb-dpms
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-dpms.so.0*

%files -n libxcb-dri2
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-dri2.so.0*

%files -n libxcb-glx
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-glx.so.0*

%files -n libxcb-randr
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-randr.so.0*

%files -n libxcb-record
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-record.so.0*

%files -n libxcb-render
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-render.so.0*

%files -n libxcb-res
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-res.so.0*

%files -n libxcb-screensaver
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-screensaver.so.0*

%files -n libxcb-shape
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-shape.so.0*

%files -n libxcb-shm
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-shm.so.0*

%files -n libxcb-sync
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-sync.so.0*

%files -n libxcb-xevie
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xevie.so.0*

%files -n libxcb-xf86dri
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xf86dri.so.*

%files -n libxcb-xfixes
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xfixes.so.*

%files -n libxcb-xinerama
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xinerama.so.0*

%files -n libxcb-xprint
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xprint.so.0*

%files -n libxcb-xtest
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xtest.so.0*

%files -n libxcb-xv
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xv.so.0*

%files -n libxcb-xvmc
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root)
%{_libdir}/libxcb-xvmc.so.0*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/xcb
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/xcb*.pc
%_docdir/%{name}

%docs_package

%changelog
