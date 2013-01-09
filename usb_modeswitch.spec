Name:		usb_modeswitch
Summary:	Activating Switchable USB Devices on Linux
Version:	1.2.3
Release:	2
License:	GPLv2+
%define fname	usb-modeswitch
%define	fver	%{version}
Source0:	http://www.draisberghof.de/usb_modeswitch/%{fname}-%{version}.tar.bz2
# (proyvind): fix a warning revealed with optimizations enabled and enable them
#             by default so that they'll get catched by upstream in the future.
#             Submitted upstream
#Patch0:		usb-modeswitch-1.1.9-catch-and-fix-more-warnings.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
Group:		System/Configuration/Hardware
BuildRequires:	libusb-devel
Requires:	sysfsutils
Requires(pre):       tcl
Requires:	usb_modeswitch-data >= 20110805

%description
USB_ModeSwitch is a mode switching tool for controlling "flip flop"
(multiple device) USB gear.

Several new USB devices (especially high-speed wireless WAN stuff,
they're expensive anyway) have their Windows drivers onboard; when
plugged in for the first time they act like a flash storage and start
installing the driver from there. After that (and on every consecutive
plugging) this driver switches the mode internally, the storage device
vanishes (in most cases), and a new device (like an USB modem) shows
up. The WWAN gear maker Option calls that feature "ZeroCD (TM)".

%prep
%setup -q -n %{fname}-%{version}
#patch0 -p1 -b .warnings~

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf


%changelog
* Sat Aug 06 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.9-1
+ Revision: 693534
- bump require on usb_modeswitch version
- regenerate P0 and also try make upstream not to strip binaries themself
  new version

* Tue Jul 05 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.8-1
+ Revision: 688823
- new version

* Mon May 02 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.7-3
+ Revision: 662615
- remove legacy rpm stuff
- fix issues when problem getting interface class breaking ie. GT-B3730

* Mon Mar 28 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.7-2
+ Revision: 648696
- add versioned minimum dependency

* Mon Mar 28 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.7-1
+ Revision: 648694
- new version

* Fri Dec 03 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.1.5-1mdv2011.0
+ Revision: 606879
- Updated to 1.1.5.

* Thu Sep 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.4-2mdv2011.0
+ Revision: 575490
- fix a compile warning and make similar warnings reveal themsel by default (P0)
- split out data

* Sun Aug 29 2010 Emmanuel Andry <eandry@mandriva.org> 1.1.4-1mdv2011.0
+ Revision: 574156
- New version 1.1.4
- new data 20100826
- drop p0 and p1, merged upstream
- drop p2, fixed upstream

* Fri Aug 13 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.3-1mdv2011.0
+ Revision: 569350
- just add a patch for upstream to not mistakenly pass libusb linkage as CFLAGS
- fix quirks with samsung 4g patch...
- add support for --waitbefore & --resetnew (P1)
- add support for Samsung GT-B3730 4G modem (P0)
- don't change order of udev rule from upstream
- new release 1.1.3
  * don't mark udev rules & usb_modeswitch.d files as config files
  * install stuff to standard locations
- ditch non-required build dependency on kernel-source
- correctify license (GPLv2 -> GPLv2+)
- build with standard cflags & ldflags

* Sat Mar 20 2010 Emmanuel Andry <eandry@mandriva.org> 1.1.1-1mdv2010.1
+ Revision: 525497
- New version 1.1.1

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - bump release

* Mon Jan 25 2010 Giuseppe Ghibò <ghibo@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 496289
- New release 1.1.0.
- New udev rules for devices in /etc/usb_modeswitch.d.
- Add tcl in Requires for the /lib/udev/usb_modeswitch wrapper.

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 1.0.7-1mdv2010.1
+ Revision: 493289
- update to new version 1.0.7

* Sun Sep 20 2009 Frederik Himpe <fhimpe@mandriva.org> 1.0.5-1mdv2010.0
+ Revision: 444922
- Update to new version 1.0.5

* Wed May 27 2009 Olivier Blin <blino@mandriva.org> 0.9.7-1mdv2010.0
+ Revision: 380126
- 0.9.7 (with automatic default endpoint detection)
- remove patch defaulting to gtmax72 config, keep upstream config

* Sat Apr 12 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.9.4-0.beta2.1mdv2009.0
+ Revision: 192605
- Update to release 0.9.4beta2.
- import usb_modeswitch


* Sat Apr 12 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.9.3-1mdv2008.1
- Initial release.
