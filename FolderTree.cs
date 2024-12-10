using System;
using System.IO;
using System.Text;

namespace ShwaTech {
    public class FolderTree {
        private DirectoryInfo _root;
        private StreamWriter _text;
        private FolderTree() { }
        public FolderTree( string path ) { _root = new DirectoryInfo( path ); }
        public void Prune() {
            using( _text = new StreamWriter( "EmptyFolders.txt" ) ) {
                PruneRecursive( _root );
            }
        }
        private void PruneRecursive( DirectoryInfo root ) {
            var subs = root.GetDirectories();
            foreach( var s in subs ) {
                PruneRecursive( s );
            }
            if( subs.Length > 0 ) {
                subs = root.GetDirectories();
            }
            if( subs.Length <= 0 ) {
                var files = root.GetFiles();
                if( files.Length <= 0 ) {
                    try {
                        _text.WriteLine( root.FullName );
                        Console.WriteLine( "{0}", root.FullName );
                        root.Delete();
                    } catch {
                        // Directory not empty
                    }
                }
            } else {
                // Directory not empty
            }
        }
    }
}