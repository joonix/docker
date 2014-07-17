#!/usr/bin/env python

import os
import time
import requests
import boto.ec2

class AuthException(Exception):
	pass

class MountException(Exception):
	pass

def mount(aws, instance_id, volume_id, path='/dev/sdf'):
	"""
	Mount the specified volume on the specified instance
	using initialized aws client.
	"""
	print aws, instance_id, volume_id
	curr_vol = conn.get_all_volumes([volume_id])[0]
	if curr_vol.status != 'available':
		curr_vol.detach()
		for retries in xrange(60):
			if curr_vol.status == 'available':
				break
			if retries == 59:
				raise MountException('Timed out waiting for volume to become available')
			time.sleep(1)
			curr_vol.update()

	return conn.attach_volume(volume_id, instance_id, path)


if __name__ == '__main__':
	access_key = os.getenv('AWS_ACCESS_KEY', None)
	secret_key = os.getenv('AWS_SECRET_KEY', None)

	if not access_key or not secret_key:
		raise AuthException(
			'You need to set credentials using AWS_ACCESS_KEY and AWS_SECRET_KEY environment vars')

	volume_id = os.getenv('AWS_VOLUME_ID')
	instance_id = requests.get('http://169.254.169.254/latest/meta-data/instance-id').text
	region = os.getenv('AWS_REGION', 'eu-west-1')

	conn = boto.ec2.connect_to_region(
		region,
		aws_access_key_id=access_key,
		aws_secret_access_key=secret_key)

	# Hook up our permanent storage
	print mount(conn, instance_id, volume_id)