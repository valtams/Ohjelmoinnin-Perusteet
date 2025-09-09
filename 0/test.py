# --------------------------------------------------------------
#  twitch_user_id.py
# --------------------------------------------------------------
import requests
import json
import sys
from typing import Optional

# Your own credentials – keep these in a separate, non‑committed file.
# Example:  creds.py  →  appID = "my-client-id";  aat = "Bearer <token>"
from creds import appID, aat

# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------
HELIX_BASE = "https://api.twitch.tv/helix"
HEADERS = {
    "Client-ID": appID,
    "Authorization": aat,          # e.g. "Bearer abcdef12345"
}
TIMEOUT = 10                       # seconds – avoids hanging forever


# ----------------------------------------------------------------------
# Helper: fetch the Twitch user ID for a given login name
# ----------------------------------------------------------------------
def get_user_id(channel_name: str) -> Optional[str]:
    """
    Calls the Helix `/users` endpoint.
    Returns the user ID as a string if the channel exists,
    otherwise returns None.
    """
    url = f"{HELIX_BASE}/users?login={channel_name}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    except requests.RequestException as exc:
        # Network‑level problems (DNS failure, timeout, connection reset, …)
        print(f"[❗] Network error while contacting Twitch: {exc}", file=sys.stderr)
        return None

    # ------------------------------------------------------------------
    # 1️⃣  HTTP status‑code handling
    # ------------------------------------------------------------------
    if response.status_code != 200:
        # Twitch returns useful JSON even on errors – try to surface it.
        try:
            err_payload = response.json()
            err_msg = err_payload.get("message", response.text)
        except (ValueError, json.JSONDecodeError):
            err_msg = response.text

        print(
            f"[❗] Twitch API responded with {response.status_code} ({response.reason}). "
            f"Details: {err_msg}",
            file=sys.stderr,
        )
        return None

    # ------------------------------------------------------------------
    # 2️⃣  Parse the JSON payload
    # ------------------------------------------------------------------
    try:
        payload = response.json()
    except (ValueError, json.JSONDecodeError):
        print("[❗] Failed to decode JSON response from Twitch.", file=sys.stderr)
        return None

    # ------------------------------------------------------------------
    # 3️⃣  Validate that a user was actually found
    # ------------------------------------------------------------------
    data = payload.get("data", [])
    if not data:
        # Empty list → the login name does not exist on Twitch.
        print(f"[⚠️] No Twitch channel found for name '{channel_name}'.", file=sys.stderr)
        return None

    # At this point we know there is at least one entry; the first is the match.
    return data[0].get("id")


# ----------------------------------------------------------------------
# Main program
# ----------------------------------------------------------------------
def main() -> None:
    user_input = input("Enter Channel Name > ").strip()

    if not user_input:
        print("[⚠️] You didn’t type anything – exiting.", file=sys.stderr)
        return

    user_id = get_user_id(user_input)

    if user_id:
        # Successful lookup – nice, clean output for downstream scripts.
        print(f"{user_input}'s userID is {user_id}")
    else:
        # Errors were already printed inside `get_user_id`.
        # Exit with a non‑zero status so callers can detect failure.
        sys.exit(1)


if __name__ == "__main__":
    main()
