from kkbox_developer_sdk.auth_flow import KKBOXOAuth
from kkbox_developer_sdk.api import KKBOXAPI
from pprint import pprint

CLIENT_ID = 'd6f84592d791d7fb7c0ca3c54d9e3a78'
CLIENT_SECRET = 'cc2e65a48702968646c23ebc6e6de3ee'

auth = KKBOXOAuth(CLIENT_ID, CLIENT_SECRET)
token = auth.fetch_access_token_by_client_credentials()
print(token.access_token)

kkboxapi = KKBOXAPI(token)

search_results = kkboxapi.search_fetcher.search('workout', types=['playlist'], terr='TW')
playlists = search_results['playlists']['data']
pprint(playlists[0], depth=3)

tracks_paging = kkboxapi.shared_playlist_fetcher.fetch_tracks_of_shared_playlists(
    playlists[0]['id'])

pprint(tracks_paging)
