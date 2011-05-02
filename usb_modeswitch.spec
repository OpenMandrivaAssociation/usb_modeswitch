Name:		usb_modeswitch
Summary:	Activating Switchable USB Devices on Linux
Version:	1.1.7
Release:	3
License:	GPLv2+
%define fname	usb-modeswitch
%define	fver	%{version}
Source0:	http://www.draisberghof.de/usb_modeswitch/%{fname}-%{version}.tar.bz2
# (proyvind): fix a warning revealed with optimizations enabled and enable them
#             by default so that they'll get catched by upstream in the future.
#             Submitted upstream
Patch0:		usb-modeswitch-1.1.7-catch-and-fix-more-warnings.patch
Patch1:		usb-modeswitch-1.1.7-dont-exit-on-interface-class-error.patch
URL:		http://www.draisberghof.de/usb_modeswitch/
Group:		System/Configuration/Hardware
BuildRequires:	libusb-devel
Requires:	sysfsutils
Requires:	usb_modeswitch-data >= 20110227

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
%patch0 -p1 -b .warnings~
%patch1 -p1 -b .interface~

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
/lib/udev/usb_modeswitch
%{_sbindir}/*
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/usb_modeswitch.conf
