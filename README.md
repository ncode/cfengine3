# Python CFEngine3 Module Protocol

A simple way to extend your cfengine3 using python

## Requirements:

* Python
* CFengine3 

## Install:

    $ python setup.py build
    $ python setup.py install

## Usage:
### Python:

    $ vim get_users
    #!/usr/bin/python

    import pwd
    import cfengine3

    if __name__ == '__main__':

        cf3 = cfengine3.protocol()
        users = [ user[0] for user in  pwd.getpwall() ]
        cf3.classes('system_users','define')
        cf3.scalar('count', '%s' % len(users))
        cf3.list('users', users)

### CFEngine3:

    $ vim example-module.cf
    body common control {
        bundlesequence  => { "load", "run" };
    }
    
    bundle agent load {
        commands:
            "$(sys.workdir)/modules/get_users" module => "true";
    
        reports:
            system_users::
                "This machine has $(get_users.count) users in /etc/passwd";
    }
    
    bundle agent run {
        vars:
            "users" slist => { @(get_users.users) };
    
        reports:
            system_users::
              "user: $(users)";
    }

### Output:

    $ cp examples/get_users /var/cfengine/modules/
    $ cf-agent -KI -f $PWD/example-module.cf 
     -> Executing '/var/cfengine/modules/get_users' ...(timeout=-678,owner=-1,group=-1)
    M "/var/cfengine/modules/get_users":
     -> Completed execution of /var/cfengine/modules/get_users
    R: This machine has 36 users in /etc/passwd
    R: user: root
    R: user: daemon
    R: user: bin
    R: user: sys
    ....

    \o/
