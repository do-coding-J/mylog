#define MODULE

#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/version.h>

MODULE_LICENSE("GPL");

static int  hello_init(void)
{
    printk(KERN_ALERT "Hello, wrold\n");
    return 0;
}

static int hello_exit(void)
{
    printk(KERN_ALERT "GoodBye, cruel world\n");
}

module_init(hello_init);
module_deinit(hello_exit);