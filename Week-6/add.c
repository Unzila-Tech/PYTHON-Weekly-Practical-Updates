#include <stdio.h>
int main() {
    int ip[4], mask[4];
    int net[4], broad[4], first[4], last[4];
    int cidr = 0, hosts, i;
    printf("Enter IP (e.g. 192.168.1.10): ");
    scanf("%d.%d.%d.%d", &ip[0], &ip[1], &ip[2], &ip[3]);
    printf("Enter Subnet Mask (e.g. 255.255.255.0): ");
    scanf("%d.%d.%d.%d", &mask[0], &mask[1], &mask[2], &mask[3]);
    for (i = 0; i < 4; i++) {
        net[i] = ip[i] & mask[i];
        broad[i] = net[i] | (255 - mask[i]);
        int m = mask[i];
        while (m) {
            cidr += m & 1;
            m >>= 1;
        }
    }
    for (i = 0; i < 4; i++) {
        first[i] = net[i];
        last[i] = broad[i];
    }
    first[3] += 1;
    last[3] -= 1;
    hosts = 1;
    for (i = 0; i < (32 - cidr); i++) hosts *= 2;
    hosts = hosts - 2;
    if (hosts < 0) hosts = 0;
    printf("\nNetwork ID: %d.%d.%d.%d\n", net[0], net[1], net[2], net[3]);
    printf("Broadcast Address: %d.%d.%d.%d\n", broad[0], broad[1], broad[2], broad[3]);
    printf("First Host: %d.%d.%d.%d\n", first[0], first[1], first[2], first[3]);
    printf("Last Host: %d.%d.%d.%d\n", last[0], last[1], last[2], last[3]);
    printf("CIDR Notation: /%d\n", cidr);
    printf("No. of Valid Hosts: %d\n", hosts);
    if (ip[0] >= 0 && ip[0] <= 127) printf("Class: A\n");
    else if (ip[0] <= 191) printf("Class: B\n");
    else if (ip[0] <= 223) printf("Class: C\n");
    else if (ip[0] <= 239) printf("Class: D\n");
    else printf("Class: E\n");
    return 0;
}

