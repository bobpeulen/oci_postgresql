# Codex

Topic 1: Primary & Reader Endpoint
Description of what visually should be shown: The client. The primary and reader endpoint with the 4 nodes. Connected through dots. Every second, a message/query should be visually distributed across the primary or reader endpoints, randomly. In addition, every 3 seconds, one read-only nodes should be deleted from the view and then added again. You can even delete all read-only nodes and then start adding them up to 4 nodes in total again.

Topic 2: Zero RPO and Highly Available
Description of what visually should be shown: Keep showing the nodes, endpoints, and client. But now, also the storage attached to the nodes should be shown as a "shared storage". The point is to show that the data is highly available, even when an individual node goes down. There should be ongoing moving queries/parts, that explain this blog clearly and very visually.
Use this blog: https://blogs.oracle.com/cloud-infrastructure/first-principles-optimizing-postgresql-for-the-cloud


Topic 3: Dynamic Storage Scaling
Description of what visually should be shown: Keep the nodes, client, endpoints and the shared storage. The focus should only be on showing that when running inserts, the database grows, and your bill grows with it. However, when removing tables, deleting data, your bill decreases as well. You only pay for what you use. Very visually, the storage should scale up and down every few seconds, with eg +200GB, -100GB, +334GB, randomly. 


Topic 4: Automated and Fast Failover
Description of what visually should be shown: Only show the client, endpoints, and the 4 nodes. Build 2 scenarios. 1st = Primary failover. 2nd = Read-only failover. For both scenarios, the visualisation should show 1 node go to "Unhealthy" and become inactive. So no traffic should flow to that unhealthy node. Important. Traffic should remain to flow from client to endpoints into the available/healthy nodes. For scenario 1: a read-only node is "Promoted" quickly as a the read/write node. And afterwards, a new read-only node is spun up to replace previously promoted read-only node so all nodes are back up and total 4. For scenario 2. a healthy read-only node is spun up while traffic keeps flowing to the other read-only nodes and the unhealthy nodes is removed.
It should be clear that all nodes, especially the healthy ones, keep having access to the shared storage.

Topic 5: Database Optimized Storage
Description of what visually should be shown: OCI PostgreSQL uses performance tiers as described here https://docs.oracle.com/en-us/iaas/Content/postgresql/performance-tiers.htm. Ranging from 75K IOPS to 750 IOPs. In some way, make it very visual that the performance is guaranteed irrespective of the database size. And that clients can choose different IOPs.

Topic 6: Cross Region Warm Standby
Description: use the information on this page to build a similar scenario like the other topics, showcasing OCI PostgreSLQ support cross region standby. Use eg Amsterdam and Frankfurt as regions. Show the database instances in the different regions can be different shapes (eg large and small). Show in a flow that a standalone gets promoted to "Primary" (in Frankfurt) and the warm standby in Amsterdam is attached and in sync. Show the warm standby has only read-only nodes. https://docs.oracle.com/en-us/iaas/Content/postgresql/cross-region-replication.htm

Topic 7: Automated Backups & PITR
Description: 

Topic 8: Query Insights & Monitoring

Topic 9: Configurations & Extensions

Topic 10: Pricing
