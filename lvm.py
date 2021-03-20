import subprocess as sp

def create_lv():
    lv_name = input("\n\tEnter lv name-->>")
    lv_size = input("\tEnter lv size -->>")
    vg_name = input("\tEnter the VG name -->>")

    try:
        op = sp.getoutput("lvcreate --size {} --name {} {}".format(lv_size, lv_name, vg_name))
        print(op)
        print("{} created successfully\n".format(lv_name))
        op = sp.getoutput("mkfs.ext4 /dev/{}/{}".format(vg_name,lv_name))
        print()

    except:
        print("Please enter correct size and vg name\n")

    return

def create_pv():
    try:
        disk_name = input("\n\tEnter partitioned disk name -->>")

        op = sp.getoutput("pvcreate {}".format(disk_name))
        print(op,"\n")

    except:
        print("Enter valid disk name!\n")

    return

def create_vg():

    try:
        vg_name = input("\t Enter VG name to be created -->>")
        pv_name = input("\t Enter PV name -->>")
        op = sp.getoutput("vgcreate {} {}".format(vg_name, pv_name))
        print(op,"\n")

    except:
        print("Enter valid disk name!\n")

    return

def extend_lv():
    try:
        lv_name = input("\tEnter LV name -->>")
        size = input("\tSize to be added/extended -->>")

        op = sp.getoutput("lvextend --size +{} {}".format(size, lv_name))
        print(op,"\n")

        o_format = sp.getoutput("resize2fs {}".format(lv_name))
        print(o_format,"\n")

    except:
        print("Plz Enter correct disk name, size!\n")

    return

def extend_vg():

    try:
        vg_name = input("\tEnter VG name -->>")
        pv= input("\tEnter PV to be added -->>")
        op = sp.getoutput("vgextend {} {}".format(vg_name, pv))
        print(op,"\n")

    except:
        print("Plz Enter correct vg name or pv to be added!\n")

    return

def reduce_lv():

    print("\nFirst make the LV offline => unmount\n")

    stat = 0
    while stat != "unmounted":
        stat = unmnt_or_mnt()

    try:

        lv_name = input("\t Enter LV name -->> ")
        op = sp.getoutput("e2fsck -f {}".format(lv_name))
        print(op)

        red_size = input("\t Enter size to be reduced -->> ")
        op = sp.getoutput("resize2fs -f {} {}".format(lv_name, red_size))
        print(op)

        lv_size = input("\t Enter size of LV after reduction -->> ")

        op = sp.getoutput("lvreduce --size {} {} -f -y".format( lv_size, lv_name))
        print(op,"\n")
        
        op = sp.getoutput("resize2fs {}".format(lv_name))
        print(op)
        
    except:
        print("\n\tPlease ente correct details!\n")

    return

def unmnt_or_mnt():
    print("\t Select any of the following:")
    print("\t 1: Mount LV")
    print("\t 2: unmount LV")
    subinp = input("\t\t-->>")
    try:
        subinp = int(subinp)
        if subinp == 1:
            mnt_pnt = input("\tEnter the mount point -->> ")
            lv_name = input("\tEnter the LV to be mounted -->> ")
            op = sp.getoutput("mount {} {}".format(lv_name, mnt_pnt))
            print(op)

            return 1
        elif subinp == 2:
            mnt_pnt =  input("\tEnter the mount point -->> ")
            op = sp.getoutput("umount {}".format(mnt_pnt))
            print(op)
            return "unmounted"

        else:
            print("Enter correct option!\n")
            return 0

    except:
        print("Enter correct option!\n")
        return 0

    return

print("\n")
print("\t"+"--"*45)

print("\t\t\t\tWelcome to the LVM menu!!")

print("\t"+"--"*45)

print("\n")

inp = 0

while inp != 12:

    print("\tSelect any of the following options:-\n")

    print("\t"+"--"*45)

    print("\t 1 : To see the disk partition table\n")

    print("\t 2 : To see the physical volumes(PV)")
    print("\t 3 : To see the logical volumes(LV)")
    print("\t 4 : To see the volume groups(VG)\n")

    print("\t 5 : To create physical volume(PV)")
    print("\t 6 : To create volume group(VG)")
    print("\t 7 : To create logical volume(LV)\n")

    print("\t 8 : To extend the volume group")
    print("\t 9 : To reduce the logical volume")
    print("\t 10 : To extend the logical volume")

    print("\t 11: Mount or unmount")

    print("\t 12 : exit\n")
    print("\t"+"--"*45)

    inp = input("\t\t--->>")

    try:
        inp = int(inp)

        if inp == 1:
            op = sp.getoutput("fdisk -l")
            print(op,"\n")

        elif inp == 2:

                print("\n\t Select any of the following")
                print("\t 1 : To see all the physical volumes(PV)")
                print("\t 2 : To see specific physical volume(PV)\n")

                subinp = input("\t--->>")
                try:
                    subinp = int(subinp)
                    #print("This is subinp:",subinp)
                    if subinp == 1:
                        op = sp.getoutput("pvdisplay")
                        print(op,"\n")

                    elif int(subinp) == 2:
                        pvinp = input("\n-->>Enter PV name")
                        try:
                            op = sp.getoutput("pvdisplay {}".format(pvinp))
                            print(op,"\n")

                        except:
                            print("!!Plzz enter the valid PV name!!\n")

                    else:
                        print("Plz enter valid option\n")

                except:
                    print("Plz enter valid option!!\n")

        elif inp == 3:

                print("\n\t Select any of the following")
                print("\t 1 : To see all the logical volumes(LV)")
                print("\t 2 : To see specific logical volume(LV)\n")

                subinp = input("\t--->>")
                try:
                    subinp = int(subinp)
                    if subinp == 1:
                        op = sp.getoutput("lvdisplay")
                        print(op,"\n")

                    elif subinp == 2:
                        lvinp = input("\n-->>Enter LV name: ")
                        try:
                            op = sp.getoutput("lvdisplay {}".format(lvinp))
                            print(op,"\n")

                        except:
                            print("!!Plzz enter the valid LV name!!\n")

                    else:
                        print("Plz enter valid option\n")

                except:
                    print("Plz enter valid option!!\n")


        elif inp == 4:

                print("\n\t Select any of the following")
                print("\t 1 : To see all the volume groups(VG)")
                print("\t 2 : To see specific volume group(VG)\n")

                subinp = input("\t--->>")
                try:
                    subinp = int(subinp)
                    if subinp == 1:
                        op = sp.getoutput("vgdisplay")
                        print(op,"\n")

                    elif subinp == 2:
                        vginp = input("\n-->>Enter VG name: ")
                        try:
                            op = sp.getoutput("vgdisplay {}".format(vginp))
                            print(op,"\n")

                        except:
                            print("!!Plzz enter the valid VG name!!\n")

                    else:
                        print("Plz enter valid option\n")

                except:
                    print("Plz enter valid option!!\n")

        elif inp == 5:
            create_pv()

        elif inp == 6:
            create_vg()

        elif inp == 7:
            create_lv()

        elif inp == 8:
            extend_vg()

        elif inp == 9:
            reduce_lv()

        elif inp == 10:
            extend_lv()

        elif inp == 11:
            unmnt_or_mnt()

        elif inp == 12:
            continue

        else:
            print("Plz enter valid option!\n")

    except:
        print("Please enter the integer\n")

