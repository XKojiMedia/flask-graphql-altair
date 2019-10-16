from flask import render_template_string

ALTAIR_VERSION = '2.3.4'

TEMPLATE = '''
<!doctype html>
<html>

<head>
  <meta charset="utf-8">
  <title>Altair</title>
  <base href="https://cdn.jsdelivr.net/npm/altair-static@{{altair_version}}/build/dist/">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <link href="https://cdn.jsdelivr.net/npm/altair-static@{{altair_version}}/build/dist/styles.css" rel="stylesheet" />
</head>

<body>
  <app-root>
    <style>
      .loading-screen {
        /*Prevents the loading screen from showing until CSS is downloaded*/
        display: none;
      }

    </style>
    <div class="loading-screen styled">
      <div class="loading-screen-inner">
        <div class="loading-screen-logo-container">
          <img src="assets/img/logo_350.svg" alt="Altair">
        </div>
        <div class="loading-screen-loading-indicator">
          <span class="loading-indicator-dot"></span>
          <span class="loading-indicator-dot"></span>
          <span class="loading-indicator-dot"></span>
        </div>
      </div>
    </div>
  </app-root>
  <script>
    window.__ALTAIR_ENDPOINT_URL__ = `{{graphql_endpoint}}`;
    // window.__ALTAIR_SUBSCRIPTIONS_ENDPOINT__ = `${subscriptionsEndpoint}`;
    // window.__ALTAIR_INITIAL_QUERY__ = `${properties.defaultQuery}`;
    // window.__ALTAIR_INITIAL_VARIABLES__ = `${properties.variables}`;
    // window.__ALTAIR_INITIAL_HEADERS__ = JSON.parse(`${headers}`);
  </script>
  <script rel="preload" as="script" type="text/javascript" src="https://cdn.jsdelivr.net/npm/altair-static@{{altair_version}}/build/dist/runtime.js"></script>
  <script rel="preload" as="script" type="text/javascript" src="https://cdn.jsdelivr.net/npm/altair-static@{{altair_version}}/build/dist/polyfills.js"></script>
  <script rel="preload" as="script" type="text/javascript" src="https://cdn.jsdelivr.net/npm/altair-static@{{altair_version}}/build/dist/main.js"></script>
</body>

</html>
'''

def render_altair(graphql_endpoint):
  graphql_endpoint = graphql_endpoint or '/endpoints'
  return render_template_string(
    TEMPLATE,
    altair_version=ALTAIR_VERSION,
    graphql_endpoint=graphql_endpoint
  )
