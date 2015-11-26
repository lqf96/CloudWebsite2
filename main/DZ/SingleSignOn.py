# Python system libraries
import base64,hmac,hashlib,urllib,json
from urlparse import parse_qs
# Django libraries
from django.http import HttpResponse,HttpResponseRedirect
# CloudWebsite settings
from CloudWebsite import settings

# Discourse SSO (Single Sign On)
def GET(request):
    # Get payload and signature from Discourse
    payload = request.GET.get('sso')
    signature = request.GET.get('sig')
    # Prompt failed if signature or payload is null
    if None in [payload,signature]:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"SSOPayloadOrSignatureNotFound"}),content_type="application/json")

    # Redirect to log-in page if user is not logged
    if ("Logged" not in request.session) or (request.session["Logged"]==False):
        login_redirect_addr = base64.encodestring(request.get_full_path())
        return HttpResponseRedirect("https://"+request.get_host()+"/accounts/login.html?Next=%s" % login_redirect_addr)

    # Validate the payload
    try:
        payload = urllib.unquote(payload)
        decoded = base64.decodestring(payload)
        assert 'nonce' in decoded
        assert len(payload) > 0
    except AssertionError:
        return HttpResponse(json.dumps({"Status":"Failed","Reason":"InvalidPayload"}),content_type="application/json")

    # Calculate signature and compare
    key = str(settings.DISCOURSE_SSO_SECRET)
    h = hmac.new(key, payload, digestmod=hashlib.sha256)
    this_signature = h.hexdigest()
    # Signature not correct
    if this_signature != signature:
        return HttpResponseBadRequest(json.dumps({"Status":"Failed","Reason":"InvalidSignature"}),content_type="application/json")

    qs = parse_qs(decoded)
    params = {
        "nonce": qs["nonce"][0],
        "email": request.session["Email"],
        "external_id": request.session["ID"],
        "username": request.session["Username"].encode("utf-8")
    }
    # Build the return payload
    return_payload = base64.encodestring(urllib.urlencode(params))
    h = hmac.new(key, return_payload, digestmod=hashlib.sha256)
    query_string = urllib.urlencode({"sso":return_payload,"sig":h.hexdigest()})

    # Redirect back to Discourse
    url = "%s/session/sso_login" % settings.DISCOURSE_BASE_URL
    return HttpResponseRedirect("%s?%s" % (url, query_string))
