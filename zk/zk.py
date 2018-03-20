from kazoo.client import KazooClient
from kazoo.security import make_acl

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()
acl = make_acl(scheme='ip', credential='172.28.0.1', read=True)
zk.set_acls(path='/test5', acls=[acl])
zk.stop()
#
# total = 0
#
# zk = KazooClient(hosts='10.6.8.92')
#
# zk.start()
#
#
# pre_time = time.time()
#
#
# def dfs(path):
#     global total
#     data, status = zk.get(path)
#     if data:
#         print(path)
#         total += 1
#
#     children = zk.get_children(path)
#
#     for child in children:
#         dfs('{}/{}'.format(path, child))
#
#
# dfs('/nxg_infra_protect')
#
#
# clusters = zk.get_children('/nxg_infra_protect')
#
# for cluster in clusters:
#     cluster_path = '/nxg_infra_protect/{}'.format(cluster)
#     sites = zk.get_children(cluster_path)
#     for site in sites:
#         site_path = '{}/{}'.format(cluster_path, site)
#         result = zk.get(site_path)
#
#         host_path = '{}/host'.format(site_path)
#         if zk.exists(host_path):
#             hosts = zk.get_children(host_path)
#             for host in hosts:
#                 result = zk.get('{}/{}'.format(host_path, host))
#
#         network_path = '{}/network'.format(site_path)
#
#         if zk.exists(network_path):
#             networks = zk.get_children(network_path)
#             for network in networks:
#                 result = zk.get('{}/{}'.format(network_path, network))
#
#
# zk.stop()
#
# print(time.time() - pre_time)
#
# print(total)
