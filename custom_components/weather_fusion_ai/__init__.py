# ******************************************************************************
# @copyright (C) 2025 Zara-Toorox - Weather Fusion AI
# * This program is protected by a Proprietary Non-Commercial License.
# 1. Personal and Educational use only.
# 2. COMMERCIAL USE AND AI TRAINING ARE STRICTLY PROHIBITED.
# 3. Clear attribution to "Zara-Toorox" is required.
# * Full license terms: https://github.com/Zara-Toorox/weather-fusion-ai/blob/main/LICENSE
# ******************************************************************************
"""Weather Fusion AI - Multi-Source Local Weather Learning Integration.

This integration provides accurate local weather forecasts by:
1. Blending multiple weather sources (Open-Meteo, Bright Sky, wttr.in, Pirate Weather)
2. Learning from your local weather station sensors
3. Applying cloud-type-specific accuracy corrections
4. Continuously improving predictions for YOUR location

@zara
"""

# PyArmor Runtime Path Setup - MUST be before any protected module imports
import sys
from pathlib import Path as _Path
_runtime_path = str(_Path(__file__).parent)
if _runtime_path not in sys.path:
    sys.path.insert(0, _runtime_path)

# Pre-load PyArmor runtime at module level (before async event loop)
# This prevents "blocking call to open" warning from platform.libc_ver()
try:
    import pyarmor_runtime_009810  # noqa: F401
except ImportError:
    pass  # Runtime not present (development mode)

import logging
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
    DATA_DIR_NAME,
    PLATFORMS,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up Weather Fusion AI from yaml configuration (not used)."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Weather Fusion AI from a config entry."""
    _LOGGER.info("Setting up Weather Fusion AI integration")

    hass.data.setdefault(DOMAIN, {})

    # Create data directory for this entry
    data_dir = Path(hass.config.path(DATA_DIR_NAME)) / entry.entry_id
    data_dir.mkdir(parents=True, exist_ok=True)

    # Import coordinator here to avoid circular imports
    from .coordinator import WeatherFusionCoordinator

    # Create coordinator
    coordinator = WeatherFusionCoordinator(
        hass=hass,
        entry=entry,
        data_dir=data_dir,
    )

    # Initialize coordinator (loads caches, sets up experts)
    await coordinator.async_initialize()

    # First data fetch
    await coordinator.async_config_entry_first_refresh()

    # Store coordinator for platforms
    hass.data[DOMAIN][entry.entry_id] = {
        "coordinator": coordinator,
        "data_dir": data_dir,
    }

    # Set up platforms (weather, sensor)
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    # Register update listener for options changes
    entry.async_on_unload(entry.add_update_listener(async_update_options))

    _LOGGER.info(
        "Weather Fusion AI setup complete for '%s' (lat=%.4f, lon=%.4f)",
        entry.data.get("location_name", "Home"),
        entry.data.get("latitude", hass.config.latitude),
        entry.data.get("longitude", hass.config.longitude),
    )

    return True


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    _LOGGER.debug("Options updated, reloading integration")
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.info("Unloading Weather Fusion AI integration")

    # Unload platforms
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        # Clean up stored data
        coordinator = hass.data[DOMAIN][entry.entry_id].get("coordinator")
        if coordinator:
            await coordinator.async_shutdown()

        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok


async def async_remove_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle removal of an entry - clean up data files if desired."""
    # Note: We don't delete the data directory by default
    # to preserve learned data in case user re-adds the integration
    _LOGGER.info(
        "Weather Fusion AI entry removed. Data preserved in %s/%s",
        DATA_DIR_NAME,
        entry.entry_id,
    )
