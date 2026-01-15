from typing import TYPE_CHECKING

from archinstall.lib.output import debug
from archinstall.lib.models.application import ApplicationConfiguration

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class CameraApp:
	@property
	def packages(self) -> list[str]:
		return ['libcamera', 'libcamera-ipa', 'libcamera-tools', 'gst-plugin-libcamera']

	@property
	def pipewire_plugin(self) -> list[str]:
		return ['pipewire-libcamera']

	def install(self, install_session: 'Installer') -> None:
		debug('Installing libcamera')
		install_session.add_additional_packages(self.packages)
		if app_config.audio_config.audio == Audio.PIPEWIRE:
			debug('Installing pipewire-libcamera plugin')
			install_session.add_additional_packages(self.pipewire_plugin)
