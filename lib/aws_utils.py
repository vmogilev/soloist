import boto3


def s3sign_url(key, bucket, expires=3600):
    """Generate the URL to get `key` from `bucket` and expire in `expires` seconds (1 hour default)"""
    s3 = boto3.client('s3')

    # Generate the URL to get 'key-name' from 'bucket-name'
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket,
            'Key': key
        },
        ExpiresIn=expires
    )

    return url
