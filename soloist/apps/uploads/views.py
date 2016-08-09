from django.shortcuts import redirect
from django.conf import settings

from lib.aws_utils import s3sign_url


def download(request, cpa_id, file_name):
    """Calls URL Signer on `file_name` and redirects to that url"""

    # example file = 'uploads/1004/3935.rmon.zip'
    file = "{}/{}/{}".format(settings.S3_UPLOAD_PREFIX, cpa_id, file_name)

    url = s3sign_url(file, settings.S3_UPLOAD_BUCKET)

    return redirect(url)
